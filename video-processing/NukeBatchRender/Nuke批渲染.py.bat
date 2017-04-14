# usr/bin/env python
# -*- coding=UTF-8 -*-
# Nuke Batch Render
# Version 2.12
'''
REM load py script from bat
@ECHO OFF & CHCP 936 & CLS
REM Read ini
REM Won't support same variable name in diffrent block
FOR /F "usebackq eol=; tokens=1,* delims==" %%a IN ("%~dp0path.ini") DO (
    IF NOT "%%b"=="" (
        SET "%%a=%%b"
    )
)

CALL :getPythonPath %NUKE%
START "NukeBatchRender" %PYTHON% %0 %*
IF %ERRORLEVEL% == 0 (
    GOTO :EOF
) ELSE (
    ECHO.
    ECHO **ERROR** - NUKE path in path.ini not Correct.
    ECHO.
    EXPLORER path.ini
    PAUSE & GOTO :EOF
)
GOTO :EOF

:getPythonPath
SET "PYTHON="%~dp1python.exe""
GOTO :EOF
'''
import os
import sys
import re
import logging
import logging.handlers
import shutil
import time
import datetime
import io
from subprocess import call, Popen, PIPE

os.chdir(os.path.dirname(__file__))

# Startup
VERSION = 2.12
prompt_codec = 'gbk'
script_codec = 'UTF-8'
call(u'CHCP cp936 & TITLE Nuke批渲染_v{} & CLS'.format(VERSION).encode(prompt_codec), shell=True)
render_time = time.strftime('%y%m%d_%H%M')
LOG_FILENAME = u'Nuke批渲染.log'

# SingleInstance
call(u'TASKKILL /FI "IMAGENAME eq 自动关闭崩溃提示.exe"'.encode(prompt_codec), stdout=PIPE, stderr=PIPE)
time.sleep(0.1)
if os.path.exists(LOG_FILENAME):
    try:
        new_name = LOG_FILENAME + render_time
        os.rename(LOG_FILENAME, new_name)
        os.rename(new_name, LOG_FILENAME)  
    except WindowsError:
        print('**提示** 已经在运行另一个渲染了, 可以直接添加新文件到此文件夹。不要运行多个。'.decode(script_codec).encode(prompt_codec))
        call('PAUSE', shell=True)
        exit()

# Set logger

# Rotate log
if os.path.exists(LOG_FILENAME):
    if os.stat(LOG_FILENAME).st_size > 10000:
        logname = os.path.splitext(LOG_FILENAME)[0]
        if os.path.exists(u'{}.{}.log'.format(logname, 5)):
            os.remove(u'{}.{}.log'.format(logname, 5))
        for i in range(5)[:0:-1]:
            old_name = u'{}.{}.log'.format(logname, i)
            new_name = u'{}.{}.log'.format(logname, i+1)
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
        os.rename(LOG_FILENAME, u'{}.{}.log'.format(logname, 1))

logfile = open(LOG_FILENAME, 'a')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_FILENAME)
formatter = logging.Formatter('[%(asctime)s]\t%(levelname)10s:\t%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Read ini

NUKE = None

def readINI(ini_file='path.ini'):
    with open(ini_file, 'r') as ini_file:
        for line in ini_file.readlines():
            result = re.match('^([^;].*)=(.*)', line)
            if result:
                var_name = result.group(1)
                var_value = result.group(2)
                globals()[var_name] = var_value
                logger.debug('{}: {}'.format(var_name, var_value))
    print('')

readINI()

# Define functions

def print_(obj):
    print(str(obj).decode(script_codec).encode(prompt_codec))

def pause():
    call('PAUSE', shell=True)
    
class nukeBatchRender(object):
    def __init__(self, dir=os.getcwd()):
        self.file_list = None
        self.error_file_list = []
        self.dir = dir

    def getFileList(self):
        file_list = list(i for i in os.listdir(self.dir) if i.endswith('.nk'))
        self.file_list = file_list
        if file_list:
            print_('将渲染以下文件:')
            for file in file_list:
                print_('\t\t\t{}'.format(file))
                logger.debug (u'发现文件:\t{}'.format(file))
            print_('总计:\t{}\n'.format(len(file_list)))
            logger.debug(u'总计:\t{}'.format(len(file_list)))
        return file_list
    
    def render(self, isProxyRender=False, isLowPriority=False):
        if not self.file_list:
            logger.warning(u'没有找到可渲染文件')
            return False
        logger.info('{:-^50s}'.format('<开始批渲染>'))
        for file in self.file_list:
            print_('## [{}/{}]\t{}'.format(self.file_list.index(file) + 1, len(self.file_list), file))
            start_time = datetime.datetime.now()
            logger.info(u'开始渲染:\t{}'.format(file))
            locked_file = file + '.lock'
            
            # Lock file
            shutil.copyfile(file, locked_file)
            file_archive_folder = 'ArchivedRenderFiles\\' + render_time
            file_archive_dest = '\\'.join([file_archive_folder, file])
            if not os.path.exists(file_archive_folder):
                os.makedirs(file_archive_folder)
            if os.path.exists(file_archive_dest):
                time_text = datetime.datetime.fromtimestamp(os.path.getctime(file_archive_dest)).strftime('%M%S_%f')
                alt_file_archive_dest = file_archive_dest + '.' + time_text
                if os.path.exists(alt_file_archive_dest):
                    os.remove(file_archive_dest)
                else:
                    os.rename(file_archive_dest, alt_file_archive_dest)
            shutil.move(file, file_archive_dest)

            # Render
            if isProxyRender:
                proxy_switch = '-p'
            else:
                proxy_switch = '-f'
            if isLowPriority:
                priority_swith = ''
            else:
                priority_swith = '-c 8G --priority low'
            if isCont:
                cont_switch = '--cont'
            else:
                cont_switch = ''
                
            proc = Popen(' '.join(i for i in [NUKE, '-x', proxy_switch, priority_swith, cont_switch, locked_file] if i), stderr=PIPE)
            
            while proc.poll() == None:
                strerr_data = proc.stderr.readline()
                if strerr_data:
                    sys.stderr.write(strerr_data)
                    logger.error(self.getErrorValue(strerr_data))

            returncode = proc.returncode
            if returncode:
                self.error_file_list.append(file)
                count = self.error_file_list.count(file)
                logger.error('渲染出错:\t{},第{}次出错'.format(file, count))
                if count >= 3:
                    logger.error('渲染出错:\t{},连续渲染错误超过3次,不再进行重试。'.format(file))
                elif os.path.exists(file):
                    os.remove(locked_file)
                else:
                    os.rename(locked_file, file)
                returncode_text = '退出码: {}'.format(returncode)
            else:
                os.remove(locked_file)
                returncode_text = '正常退出'

            end_time = datetime.datetime.now()
            total_seconds = (end_time-start_time).total_seconds()
            logger.info('总计耗时:\t{}'.format(secondsToStr(total_seconds)))
            logger.info('结束渲染:\t{}\t{}'.format(file, returncode_text))
        logger.info(u'<结束批渲染>')
    
    def checkLockFile(self):
        locked_file = list(i for i in os.listdir(self.dir) if i.endswith('.nk.lock'))
        if locked_file:
            print_('**提示** 检测到上次未正常退出所遗留的.nk.lock文件, 将自动解锁') 
            logger.info('检测到.nk.lock文件')
            for file in locked_file:
                unlocked_name = os.path.splitext(file)[0]
                if not os.path.exists(unlocked_name):
                    try:
                        os.rename(file, unlocked_name)
                        logger.info('解锁: {}'.format(file))
                    except WindowsError:
                        print_('**错误** 其他程序占用文件: {}'.format(file))
                        logger.error('其他程序占用文件: {}'.format(file))
                        pause()
                        logger.info('<退出>')
                        exit()   
                else:
                    os.remove(file)
                    logger.info('因为有更新的文件, 移除: {}'.format(file))
            print('')
    
    def getErrorValue(self, str):
        ret = str.strip('\r\n')
        ret = ret.replace('Read error: No such file or directory', '读取错误: 找不到文件或路径')
        ret = ret.replace('Missing input channel', '输入通道丢失')
        match = re.match(r'\[.*\] ERROR: (.*)', ret)
        if match:
            ret = match.group(1)
        return ret
    
def secondsToStr(seconds):
    ret = ''
    hour = int(seconds // 3600)
    minute = int(seconds % 3600 // 60)
    seconds = seconds % 60
    if hour:
        ret += '{}小时'.format(hour)
    if minute:
        ret += '{}分钟'.format(minute)
    ret += '{}秒'.format(seconds)
    return ret
        
# Display choice
logger.info('{:-^100s}'.format('<启动>'))
BatchRender = nukeBatchRender()
BatchRender.checkLockFile()
if not nukeBatchRender().getFileList():
    print_('**警告** 没有可渲染文件')
    logger.info(u'用户尝试在没有可渲染文件的情况下运行')
    pause()
    logger.info('<退出>')
    exit()

if os.path.exists('afterRender.bat'):
    print_('**提示** 将在渲染完成后自动运行afterRender.bat\n')
    
print_('方案1:\t\t\t制作模式(默认) - 流畅, 出错直接跳过\n'
       '方案2:\t\t\t午间模式 - 全速, 出错继续渲\n'
       '方案3:\t\t\t夜间模式 - 全速, 出错继续渲, 完成后休眠\n'
       '方案4:\t\t\t代理模式 - 流畅, 出错继续渲, 输出代理尺寸\n'
       '\nCtrl+C\t直接退出\n')
       
try:
    choice = call(u'CHOICE /C 1234 /T 15 /D 1 /M "选择方案"'.encode(prompt_codec))
except KeyboardInterrupt:
    exit()

print('')
isLowPriority = False
isHibernate = False
isProxyRender = False
isCont = False
if choice == 1:
    isLowPriority = True
    logger.info('用户选择:\t制作模式')
elif choice == 2:
    isCont = True
    logger.info('用户选择:\t午间模式')
elif choice == 3:
    isCont = True
    isHibernate = True
    logger.info('用户选择:\t夜间模式')
elif choice == 4:
    isCont = True
    isProxyRender = True
    isLowPriority = True
    logger.info('用户选择:\t代理模式')
else:
    exit()

# Main
try:
    autoclose = None
    if os.path.exists(u'自动关闭崩溃提示.exe'.encode(prompt_codec)):
        autoclose = Popen(u'自动关闭崩溃提示.exe'.encode(prompt_codec))

    while BatchRender.getFileList():
        BatchRender.render(isProxyRender, isLowPriority)

    if os.path.exists('afterRender.bat'):
        call('afterRender.bat')

    if isHibernate:
        choice = call(u'CHOICE /t 15 /d y /m "即将自动休眠"'.encode(prompt_codec))
        if choice == 2:
            pause()
        else:
            logger.info('<计算机进入休眠模式>')
            print_('[{}]\t计算机进入休眠模式'.format(time.strftime('%H:%M:%S')))
            call(['SHUTDOWN', '/h'])
    else:
        choice = call(u'CHOICE /t 15 /d y /m "此窗口将自动关闭"'.encode(prompt_codec))
        if choice == 2:
            pause()

    logger.info('<退出>')
    exit()
except SystemExit as e:
    Popen('EXPLORER {}'.format(LOG_FILENAME.encode(prompt_codec)))
    if autoclose:
        autoclose.kill()
    exit(e)
except:
    import traceback
    traceback.print_exc()
    pause()
    logger.error('本程序报错')
    traceback.print_exc(file=logfile)

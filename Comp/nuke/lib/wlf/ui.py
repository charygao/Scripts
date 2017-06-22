# -*- coding: UTF-8 -*-
import os

import nuke
from autolabel import autolabel

import callback
import pref


def add_menu():
    
    def _comp(menu):
        m = menu.addMenu("合成")

        m.addCommand('创建背板', 'wlf.backdrop.create_backdrop()', 'ctrl+alt+b', icon="backdrops.png")
        m.addSeparator()
        m.addCommand('选中节点:使用相对路径', 'wlf.comp.nodes_to_relpath(nuke.selectedNodes())', 'F2', icon="utilitiesfolder.png")
        m.addCommand("选中节点:分离rgba","wlf.comp.shuffle_rgba(nuke.selectedNode())")
        m.addCommand('选中节点:分离所有通道', 'wlf.comp.split_layers(nuke.selectedNode())', 'F3',icon="SplitLayers.png")
        m.addCommand("选中节点:重命名PuzzleMatte","wlf.comp.MaskShuffle(prefix='PuzzleMatte')","F4")
        m.addSeparator()
        m.addCommand("所有读取节点:修正错误" , "wlf.comp.fix_error_read()", 'F6')
        m.addCommand("所有读取节点:检查缺帧", "wlf.dropframe.DropFrameCheck()()")
        m.addCommand("所有读取节点:序列替单帧", "wlf.comp.replace_sequence()")
        m.addSeparator()
        m.addCommand("所有节点:删除无用节点","wlf.comp.delete_unused_nodes()")
        m.addCommand("所有节点:根据背板重命名", "wlf.comp.RenameAll()" )
        m.addCommand("所有节点:根据背板分割文件", "wlf.comp.splitByBackdrop()")

    def _autocomp(menu):
        m = menu.addMenu('自动合成')
        m.addCommand('自动合成',"wlf.autocomp.Comp()()",icon='autocomp.png')
        m.addCommand('批量合成',"wlf.autocomp.Precomp().showDialog()",icon='autocomp.png')

    def _cgtw(menu):

        m = menu.addMenu('CGTeamWork', icon='cgteamwork.png')
        m.addCommand('设置工程', "wlf.cgtw.CGTeamWork.ask_database()")
        m.addCommand('添加note', "wlf.cgtw.Shot().ask_add_note()")
        m.addCommand('上传nk文件', "wlf.cgtw.Shot().upload_nk_file()")
        m.addCommand('上传单帧', "wlf.cgtw.Shot().upload_image()")
    
    def _create_node_menu():
        _plugin_path = '../../plugins'

        m = nuke.menu("Nodes")
        m = m.addMenu('吾立方', icon='Modify.png')
        os.chdir(os.path.dirname(__file__))
        
        create_menu_by_dir(m, _plugin_path)
        m.addCommand("吾立方", "nukescripts.start('http://www.wlf-studio.com/')")

    _menubar = nuke.menu("Nuke")

    _comp(_menubar)
    _autocomp(_menubar)
    _cgtw(_menubar)
    _create_node_menu()
    

def create_menu_by_dir(parent, dir):
    if not os.path.isdir(dir):
        return False
    _dir = os.path.abspath(dir)

    _order = lambda s: ('_0_' if os.path.isdir(os.path.join(_dir, s)) else '_1_') + s
    _listdir = os.listdir(_dir)
    _listdir.sort(key=_order)
    for i in _listdir:
        if i == 'icons':
            continue
        _abspath = os.path.join(_dir, i)
        _name, _ext = os.path.splitext(i)
        if os.path.isdir(_abspath):
            nuke.pluginAddPath(_abspath)
            n = parent.addMenu(i, icon='{}.png'.format(i))            
            create_menu_by_dir(n, _abspath)
        elif _ext.lower() == '.gizmo':
            parent.addCommand(_name, 'nuke.load("{}")'.format(_name), icon='{}.png'.format(_name))
            
def custom_autolabel(enable_text_style=True) :
    '''
    add addition information on Node in Gui
    '''
    a = autolabel().split( '\n' )[0]
    b = '\n'.join( autolabel().split( '\n' )[1:] )
    s = ''
    this = nuke.thisNode()
    if this.Class() == 'Keyer' :
        s = '输入通道 : ' + nuke.value( 'this.input' )
    elif this.Class() == 'Read' :
        try:
            df = this['dropframes'].value()
        except NameError:
            df = ''

        if df :
            if not this['disable'].value():
                nuke.warning( '{}: [缺帧]{}'.format(this.name(), df))

            if enable_text_style:
                df = '\n<span style=\"color:red\">缺帧:' + df + '</span>'
            else:
                df = '\n缺帧:' + df
        else :
            df = ''

        if enable_text_style:
            s = '<span style=\"color:#548DD4;font-family:微软雅黑\"><b> 帧范围 :</b></span> '\
                '<span style=\"color:red\">' + nuke.value( 'this.first' ) + ' - ' + nuke.value( 'this.last' ) + '</span>'\
                + df
        else:
            s = '帧范围 :' + nuke.value( 'this.first' ) + ' - ' + nuke.value( 'this.last' ) + df
    elif this.Class() == 'Shuffle' :
        ch = dict.fromkeys( [ 'in', 'in2', 'out', 'out2'], '' )
        for i in ch.keys() :
            v = nuke.value( 'this.' + i)
            if v != 'none':
                ch[ i ] = v + ' '
        s = ( ch[ 'in' ] + ch[ 'in2' ] + '-> ' + ch[ 'out' ] + ch[ 'out2' ] ).rstrip( ' ' )

    # join result
    if s :
        result = '\n'.join( [ a, s, b ] )
    elif b:
        result = '\n'.join( [ a, b ] )
    else :
        result = a
    result = result.rstrip( '\n' )
    return result

# -*- coding=UTF-8 -*-
"""license check. only intend to block non-programer user. """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime as time
import os
import sys

from __about__ import __version__

EXPIRE_AT = time.date(2018, 1, 1)
IS_EXPIRED = EXPIRE_AT < time.date.today()

if IS_EXPIRED:
    __import__('nuke').message(b'吾立方插件: 许可已过期, 请联系作者获取更新许可\n要卸载请直接删除文件夹:\n{}'.format(
        os.path.abspath(os.path.join(__file__, '../../'))))
    sys.exit(0)


def setup():
    print('-' * 20)
    msg = '吾立方插件 {}\n许可至: {}'.format(__version__, EXPIRE_AT)
    print(msg.encode(sys.getfilesystemencoding(), 'replace'))
    print('-' * 20)

    del globals()['EXPIRE_AT']

# -*- coding: utf-8 -*-
__author__ = 'xzq'

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main            # 主目录为启动文件目录，一切路径从这里找

if __name__ == "__main__":
    main.ArgvHandler()


# 包的导入
# _init.py 文件可以区分文件夹和包，当此文件存在是可认为是一个包
# 包- 模块- 类- 函数、变量(类的本身特性）
# import module_name(包括命名空间)，import只能导入模块

import os,sys   #添加系统的相对路径和绝对路径
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR) # 添加文件路径到系统变量中

import C1S06.C1S06test1 as aac
print(aac.b)

#from module import a    # 可以直接导入具体的变量、模块
from C1S06 import C1S06test1 as aad
print(aad.c)

# from C1S06 import *    # *可以导入全部的变量，导入的变量为C1S06中被内置模块所定义的变量
#     print(a)

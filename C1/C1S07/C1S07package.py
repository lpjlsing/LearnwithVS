# 包的导入
# _init.py 文件可以区分文件夹和包，当此文件存在是可认为是一个包
# 包- 模块- 类- 函数、变量(类的本身特性）
# import module_name(包括命名空间)，import只能导入模块
import C1S06.C1S06test1 as aac
print(aac.b)

#from module import a    # 可以直接导入具体的变量、模块
from C1S06.C1S06test1 import 

from C1S06 import * # *可以导入全部的变量，导入的变量为C1S06中被内置模块所定义的变量
    print(a)

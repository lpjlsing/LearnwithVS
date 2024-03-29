# 包导入，这里文件自动执行
# _init.py 文件可以区分文件夹和包，当此文件存在时才可认为此时的文件夹是一个包，
#          导入时文件自动执行
# 包- 模块- 类- 函数、变量(类的本身特性）
# import module_name(包括命名空间)，import只能导入模块
# _all_: 模块内置变量
# 可以在 __init__文件里配置包的一些初始化操作，比如批量导入、定义内置变量
# 导入这个包后，这个文件里的函数自动执行
# 包和模块不会被重复导入

# 避免模块间的互相循环导入
# 入口文件

import sys
import datetime
import io

print(sys.path)
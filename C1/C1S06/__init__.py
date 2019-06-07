import os,sys   #添加系统的相对路径和绝对路径
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR) # 添加文件路径到系统变量中，或者使用 cd C1S06 来定位需要的包

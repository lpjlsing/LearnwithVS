# 枚举

from enum import Enum # 枚举本身是个类,而不是一个类型。python中只有是类和对象

# 把类转为枚举类型
class VIP(Enum): # 普通类VIP通过枚举函数Enum的调用成为了枚举类 
    YYF = 1 # 枚举名称最好大写
    LONGDD = 2

print('输出枚举标签类型：')
print(VIP.YYF) # 打印出枚举的标签
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

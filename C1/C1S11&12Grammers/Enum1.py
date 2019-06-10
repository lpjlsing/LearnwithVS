""" 

枚举：保护功能 ******
Enum
IntEnum,unique

23种设计模式 单例模式 

普通类：1. 可变    2. 不能防止相同标签的出现

枚举操作： 标签.name or .value，
          除了可以进行 == 比较， is 比较，枚举类型间不能做其它条件比较
          不同枚举间互不影响
          枚举标签的 name 不能重复，vvalue可以重复且后面的枚举视为第一个出现的 别名 ******
          VIP['YYF']--> 通过name获得标签 VIP.YYF
          数字转换为枚举类型：a=1  VIP(a)   ******

枚举特征： 枚举类型、名称、值

"""

from enum import Enum # 枚举本身是个类,而不是一个类型。python中只有是类和对象
from enum import IntEnum, unique # IntEnum: 枚举类型只能是数字类型而不包括字符串str
                                 # unique:  枚举的value只能唯一


# 把类转为枚举类型
class VIP(Enum): # 普通类VIP通过枚举函数Enum的调用成为了枚举类 
    YYF = 1 # 枚举名称最好大写
    LONGDD = 2
    Zippo = 3
    DD = 4
    LONGDD2 = 2 # value重复
    Zhou = 'DG'
class Common(IntEnum):
    Zippo = 3



print('输出枚举标签类型：',VIP.YYF,type(VIP.YYF)) # 打印出枚举的标签，得到枚举类型
print('获取标签的值，字符串：', VIP.YYF.name) 
print('获取标签的值，字符串：', VIP.YYF.name,type(VIP.YYF.name)) # 得到字符串，获取标签name
print('获取标签的值，字符串：', VIP.YYF.value,type(VIP.YYF.value)) # 得到字符串，获取标签值value
print('通过标签获得枚举类型：')
print(VIP['LONGDD'])
print('~~~~~~~~~~~~~~~~~')

r = VIP.LONGDD == VIP.DD
r1 = VIP.LONGDD is VIP.DD
print('枚举间比较 == ：',r)
print('枚举间比较 is ：',r1)
print('~~~~~~~~~~~~~~~~~')

for v in VIP:
    print('遍历枚举类型：',v) # 遍历枚举类型,如VIP.YYF

for v1 in VIP.__members__.items(): # 通过内置成员函数和items输出带别名的标签
    print('通过内置 __memebers__.items遍历包括别名枚举: ',v1)

for v2 in VIP.__members__: # 通过内置成员函数标签name
    print('通过内置 __memebers__ 遍历包括别名枚举: ',v2)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')





# 类和模块全局变量和局部变量不同


# 类变量
# 实例变量

class B():
    sum = 0
    name = '' # 类变量，定义在类中，但类变量最好不要定义为特定值
    age = 0
    def __init__(self,name,age): #这个self可以定义为任意变量的标识
        self.name = name # name这个实例变量最好是定义在对象中，而不是定义在类中
        self.age = age # self声名参数可以用来保存对象的实例变量

B1 = B('b1', 19)
B2 = B('b2',20)
print(B1.name)
print(B2.name)
print(B.name)
print('~~~~~~~~~~~~~~~~~~')


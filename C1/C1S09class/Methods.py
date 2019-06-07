'''
1.类方法和静态方法

2.方法可见性

'''
#类方法
class C():
    sum2 = 0
    def __init__(self):
        self.__class__.sum2 += 1
    @classmethod  # 定义一个实例方法成为类方法
    def plus_sum2(cls):
        cls.sum2 += 1
        print(cls.sum2)
    @staticmethod
    def add(x,y): #静态方法，并没有像类方法那样把 cls 显式的传入
        print('静态方法')
        print(C.sum2) # 可以通过全局类调用来调用变量
#        print(self.sum2) # 不能再静态方法中调用实例变量


print('~~~~~~~~~~~类方法调用')

c1 = C()
# 类方法：关联类本身,如果调用跟对象无关，可以使用类方法
c1.plus_sum2()

# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~调用Ob3')
# from Ob3 import B1 
# from Ob3 import B 
# print(B1.name)
# B.plus_sum1()
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~调用Ob3')

print('~~~~~~~~~~~静态方法对象调用')
# 静态方法: 可以同时被对象和类调用，不需要显示的春如参数cls
# 静态方法中不能调用实例变量，可以通过全局类调用
c1.add(1,2)
print('~~~~~~~~~~~静态方法类调用')
C.add(1,2)


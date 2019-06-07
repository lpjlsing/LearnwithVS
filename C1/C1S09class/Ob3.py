# 类和模块全局变量和局部变量不同


# 类变量
# 实例变量

class B():
    sum1 = 0
    # name = '' # 类变量，定义在类中，但类变量最好不要定义为特定值
    # age = 0
    def __init__(self,name,age): #self可以定义为任意变量的标识
        self.name = name # name这个实例变量最好是定义在对象中，而不是定义在类中成为类变量
        self.age = age # self声名参数可以用来保存对象的实例变量
        self.__class__.sum1 += 1 # 当实例方法调用增加时，sum1函数自动增加
        print('~~~~~~~~~~~~~~~~~~类变量调用')
        print('总数sum:' + str(self.__class__.sum1)) # 类变量调用
        print('~~~~~~~~~~~~~~~~~~实例中调用类变量')
        print(self.__dict__) 
        print(B.sum1) # 实例方法内部调用类变量方法1
        print(self.__class__.sum1) # 实例方法内部调用类变量方法2

    @classmethod  # 定义一个实例方法成为类方法
    def plus_sum1(cls):
        cls.sum1 += 1
        print(cls.sum1)
print('~~~~~~~~~~~~~~~~~~类实例化')

# 实例方法第一个参数必须传入self
# 实例方法定义的时候 self在python中一定要出现，调用的时候不需要给self赋予实参 ******
# self为python默认的，可以更改
# self是当前调用某一个方法的对象

B1 = B('b1', 19)
print('~~~~~~~~~~~~~~~~~~第二次调用，每调用一次，构造函数自动运行一次')
B2 = B('b2',20)
print(B1.name)
print(B2.name)
#print(B.name)
print('~~~~~~~~~~~~~~~~~~打印所有实例变量')
print(B1.__dict__) # 打印出B1实类中的所有实例变量
#  #错误


# 实例方法中访问类变量，实例方法关联实例对象

print(B.sum1) # 实例方法中使用实例变量


# 类方法：关联类本身，如果调用跟对象无关，可以使用类方法
print('~~~~~~~~~~~类方法调用')
print('sum1调用的次数：')
B.plus_sum1()


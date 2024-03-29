""" 
面向对象

面向对象3大特性: 继承性，封装性，多态性

方法： 面向对象的设计层面
函数： 面向过程的层面
变量： 在类中，成为 数据成员 ，每个变量为类的一个成员

类：1.类变量和实例变量-->特征  2.方法~实例方法，类方法，静态方法-->行为  3.构造函数
    4.一个模块最好只写一个类

"""
class A():  # 类，类的参数不要有下划线，类用于 封装代码，类是实体逻辑对应的计算机逻辑反应
            # 一个模块可以定义多个类

    name = 'name1' # 这个位置的 name 为 全局变量, 类的对象，为类变量
    age = 0
    sums = 0 

    # 行为和特征是类的两大特点
    # 行为即是类中的方法def

# 实例方法定义的时候 self在python中一定要出现，调用的时候不需要给self赋予实参 ******
# self为python默认的，可以更改
# self是当前调用某一个方法的对象，跟类无关，代表实例

    def __init__(self,name,age): # 构造函数，自动调用，为实例方法
                                 #构造函数的调用通过实例化进行
                                  # 构造函数可以使模板生成不同的对象
                                  # 初始化对象的属性，初始化类的特征
                                  # name, age 为传入的参数，后续调用必需传入这两个值
        name = name #这里重新定义了name，name为方法内部实例变量
        age = age 
        self.name = name # self来保存对象的实例变量
        print('自动调用')
        return # 构造函数中，return后不能返回自定义的值，只能返回None

    def print_file(self): # 函数可以不传入参数，self为第一声明，def是类的 普通实例方法
                          # 普通的方法可以直接调用，因为传入参数后已经实例化
        print('name: ' + self.name) # self 参数把全局变量name 调用为局部变量
        print('age: ' + str(self.age))


# 类和对象
# 类为方法和特征到的抽象描述，类是一个 模板
# 象是类的具体描述，使抽象方法和特征进行实例化

a = A('name',18)  # 赋值，这里把类实例化后再调用， 类的调用最好是在类的外部调用
a.print_file() # 读取，当类中 A 没有参数，这里可以直接使用 () 来调用类中的方法def
print(id(a)) # a的内存地址
print('~~~~~~~~~~~~~~~~~~~~')
# b = a.__init__('self1',age=19) # 构造函数可以调用， 但不建议这样做
# print('b = ',b) #构造函数返回None
print('~~~~~~~~~~~~~~~~~~~~')

# 类和模块全局变量和局部变量不同



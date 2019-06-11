""" 
对修改封闭，对扩展开放

import time

装饰器：  代码复用，代码封闭安全性
    一个对象能否以装饰器形式使用的唯一原则是它构成的decorator必须callable(可被调用)  ******
    这个callable对象可以使闭包函数，也可以是class...
    不改变原有函数，增加新功能  ******
    装饰器外部函数，装饰， 跟闭包相比没有环境变量。内部函数用于封装
    @：语法糖 之一通过 @装饰器， 保持原来的调用方式不改变  ******
    @ 是AOP，python设计模式  ******
    当装饰器跟特定函数绑定时，装饰器没有意义  ******
    def wrapper2(*args,**kw): -->可以传入任意类型参数，比如 通用参数、关键字参数  ******
    在所需要函数上加入装饰器，可以通过flask是函数成为一个控制器 *****

带参数装饰器： 利用可变参数，如*args

class类作为一个装饰器： 通过__call__魔法方法

时间戳

flask：控制器

"""

import time

# 非装饰器：定义函数没有体现出与新函数的关联
def t1():
 #   print(time.time())
    print('Time is: ')
t1()   # 时间戳

def t2():
#    print(time.time())
    print('Time is: ')

def t(func): # 函数作为以一个函数的参数传入
    print(time.time())
    func()

t(t1)
t(t2)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#装饰器：

def decorator(func): # 装饰器外部函数，装饰， 跟闭包相比没有环境变量
    def wrapper(): # 内部函数，封装
        print(time.time())
        func()  # 这里把func()参数函数封装进内部函数，func作为外部函数参数
    return wrapper

def t3():
    print('Time is: ')

@decorator  # 通过@装饰器， 保持原来的调用方式不改变
            # 装饰器真正意义
def t4():
    print('Time is: ')

print('这个装饰器需要通过变量来调用：')
dd = decorator(t3)
dd()  # 这个装饰器需要通过变量来调用  ******

print('装饰器通过@语法堂不改变调用方式：')
t4()  # 这个装饰器需要通过变量来调用  ******

# 带参数装饰器： 利用可变参数
print('带参数装饰器：')

def decorator2(func): # 装饰器外部函数，装饰， 跟闭包相比没有环境变量
    def wrapper2(*args,**kw): #  *args 表示通用参数，这个可以任意定义
                              #  **kw 传入关键字参数
        print(time.time())
        func(*args, **kw)  # 这里把func()参数函数封装进内部函数，func作为外部函数参数
    return wrapper2

def t5(func_name):
    print('Time is: ' + func_name)

@decorator2
def t6(func_name1,func_name2):
    print('Time is: ' + func_name1)
    print('Time is: ' + func_name2)

t5('test func')
t6('test func1','test func2')

@decorator2
def t7(func_name3,func_name2, **kw):   # 装饰器带关键字参数
                                       #
    print('Time is: ' + func_name3)
    print('Time is: ' + func_name2)
    print(kw) # 打印kw关键字参数

t7('test **kw func3','test **kw func4', a = 1, b = 2, c = 'd')

# 类作为一个装饰器： 在类的内部，通过__call__魔法方法
def __call__(self, *arg, **kw):
    pass


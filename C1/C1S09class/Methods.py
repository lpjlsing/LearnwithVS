'''
1.类方法和静态方法

2.方法可见性：函数前面不加下划线--> 公开    函数前面双下划线 __ -- > 私有  
             函数两边具有双下划线: 公开

'''
#类方法和静态方法：变量的更改最好是通过方法来实现，而不是直接在外部修改！ ******
class C():
    sum2 = 0
    def __init__(self,name, age): # __init__两边均有双下划线在python中还是公有函数
        self.name = name
        self.age = age
        self.__score = 0 # 前面双下划线，score 私有变量
        self.__class__.sum2 += 1

    def marking(self,score): # 打分
        if score < 0:
            print('Must! Score > 0!') 
            score = 0
        else: 
            self.__score = score
            print(self.name + ' 分数:' + str(self.__score))

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
c1 = C('li',27)
c2 = C('Gu',27)
# 类方法：关联类本身,如果调用跟对象无关，可以考虑使用类方法
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

print('~~~~~~~~~~~方法可见性')
# 方法可见性：帮助别人更规范的修改变量，public or private 某个变量
# print('input scores: ')
# scores = input() 
c1.marking(99)
c1.__score = -1  # 方法私有后外部访问不行，但私有实例变量仍可调用，但这里已经成为新添加的变量
                 # 由于python的动态性，这里的私有变量score为新添加的实例变量，并不是构造函数处的score
                 # 不能动态的添加私有变量，这是python对于私有变量的保护机制决定
print('~~~~~~~~~~__score外部新添加变量，__dict__查找出了新添加的__score变量')
print(c1.__score)
print(c1.__dict__)
#print(c2.__score) #c2
print('~~~~~~~~~仍然可以通过类来读取私有变量')
print(c2.__dict__)
print(c2._C__score) # python并无强制的私有变量保护机制
                    # 可以看到，这里通过类仍然能够读取到私有变量__score
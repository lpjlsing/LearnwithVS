""" 
继承
 
变量和方法均可以继承

继承开类原则

super函数作为函数内部父类的继承，更换父类时只需要更改class处父类名称即可
子类内部的父类可以通过super函数来完成自动更改调用新的父类

"""

from fatherclass import Human
 
class Student(Human): # Human为Student的父类，Human为子类
                      # 父类和子类变量可以同名，python有限调用子类方法
    # sum3 = 0
    def __init__(self,school,name,age): 
        
        # __init__两边均有双下划线在python中还是公有函数
        self.school = school

        #第一种继承
        Human.__init__(self,name,age) #子类中调用父类的参数
                                      # 子类调用时一定要传入self ******
                                      # 这里使用一个类调用了一个实例方法，为python独有
                                      # 实例化调用时python自动调用了self，
                                      # 而对父类实例方法调用时init相当于普通实例方法，此时必须传入全部变量，因此必须有self 传入
        # 第二种继承(推荐)
        super(Student,self).__init__(name,age) # super代表父类，这里代表Human
    


    def do_work(self):  #使用类调用self时，传入任意参数均可完成函数调用 ******
        print('Physics') 

s1 = Student('USTC','Gu',27) # 子类中调用父类参数是需把子类和父类所需的参数一起传入
print('~~~~~~~~~~父类可以直接输出变量到子类')
print(Student.sum3)
print(s1.name)
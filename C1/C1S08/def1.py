#函数
a = 1.2345
print(round(a,2)) # 取数值的小数点后指定的位数

def funcname(parameter_list): # 函数的参数列表可以没有，可以 return value None
    pass

# def funcname(self, parameter_list):
#     pass

# @staticmethod
# def funcname(parameter_list):
#     pass

import sys
sys.setrecursionlimit(1000) #最大递归常数

def changexy(x,y): # 交换数字 
                   # changexy(x,y)为形式参数，即形参
    x = x - y
    y = x + y
    x = y - x 
    print('x = ',x,'y = ',y)
    return x, y # return 表示此函数运行终止， return可以返回任意类型的变量， 
                # return == return None
                # return x, y才是def 定义的函数 changexy(x,y) 的返回值
                #如果只是 return , 函数的返回值只是None
print('~~~~~~~~~~~~~~~~~')

x_changexy, y_changexy = changexy(4,5) # 可以在两侧同时设定相同个数的值， tuple类似
print(x_changexy,y_changexy)

aa = ab = ac = 1 #同时定义
print(aa,ab,ac)
print('~~~~~~~~~~~~~~~~~~~~~')

# 参数传递顺序：
# 1.必须参数(形参) ， 2.关键字参数 ， 3. 默认参数 ， 

a = changexy(1,2) # changexy(1,2)为实际参数，实参，形参和实参数量一定要相同
print('add = ',a) #如果只是 return , 函数的返回值只是None

c = changexy(y=6,x=1) # 关键字参数
                      # 函数模块可以不用按照形参顺序来定义，此时 x,y仍为changexy的 x,y
print('~~~~~~~~~~~~~~~~~~~~~')

def Defaulats_(x,y=1,c=100): # 默认参数可以在必须参数、关键字参数后自动调用，可以不写
                              # 关键字参数可以不用按顺序调用
    print(x,y,c)
    return x,y,c #治理就是函数模块返回的值
moren = Defaulats_(1,2) #此时默认参数 c=100 被自动调用
print(moren)

def aaa(): # 函数可以不传入参数
    pass 
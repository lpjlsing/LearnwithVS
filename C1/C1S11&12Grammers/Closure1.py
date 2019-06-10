""" 
一切皆对象

函数式编程：  (VS. 命令式编程)  ******

lisp: 人工智能使用较多

1. 闭包： = 函数+环境变量，环境变量需要被函数引用才能使闭包函数，JS，python中使用
        从模块函数外部间接调用函数内部变量
        如果仅是调用局部变量，函数并不是闭包函数 ******
        可以避免使用全局变量 ******
        语法框架中使用
环境变量： 在闭包外部，但非全局变量，
__closure__[0].cell_contents： 可以查询第 [0] 个环境变量内存位置和具体的值

闭包环境变量可以保存上一次调用的状态！！！   ******

nonlocal：强制使变量为 非本地局部变量

(return 变量, 函数) --> 返回了元组类型

2. 匿名函数：



"""
#闭包

def curve_pre():
    a = 3 # 闭包环境变量，常驻内存，可能出现内存泄漏 ******
    b = 7
    def curve(x): # 闭包函数
        y = a * x * x # 等号左边python默认是局部变量
                      # 当有局部变量后，程序并不会去外部寻找所需变量
        b = 5 # 这里的b是 局部变量， 并不是闭包，与这个函数最后返回的结果无关 ******
              # 如果删除这个局部变量，则仍为闭包，则当调用b时b才是环境变量，curve_pre()才能使一个闭包
        print('闭包内函数变量与环境变量相同时：',b)
        return y 
        return curve # 闭包函数的返回值没特殊地方，跟非闭包的一样
    print('闭包内部函数外部变量：',b)
    curve(2)
    return curve # 返回函数，形成闭包
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

a = 4
f = curve_pre()
f(1)
print(f(3))
print( '输出闭包环境变量保存的位置：',f.__closure__)  # 输出闭包环境变量保存的位置
print('闭包第0个环境变量，输出它的值：',f.__closure__[0].cell_contents) # 第0个环境变量，输出它的值
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 旅行者问题
origin = 0 # 全局变量，全局环境变量

# 非闭包实现旅行者问题：
def go(step):
    global origin # 全局变量声明
    new_pos = origin + step 
    origin = new_pos
    return new_pos, origin, go # return 变量, 函数 --> 返回了元组类型
 #   return go
# 闭包实现：
def factory(pos): # 工厂模式
    def go(step):
        nonlocal pos # 闭包可以直接声明全局变量，不需要去直接调用闭包函数外部的全局变量 ******
                     # nonlocal声明pos不是本地局部变量，因为 factory(pos) 里面已经出现了pos
        new_pos2 = pos + step
        pos = new_pos2
        return new_pos2
    return go # 返回函数，形成闭包

tourist = factory(origin)

print('非闭包实现旅行者问题：')
print(go(2))
print(go(3))
print(go(6))
print('~~~~~~~~~~~~~')
print('闭包实现：')
print(tourist(2))
print(tourist(3))
print(tourist(6))
print('检查闭包：',tourist.__closure__[0].cell_contents)


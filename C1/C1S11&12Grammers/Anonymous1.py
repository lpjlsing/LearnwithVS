""" 
闭包

匿名函数: lambda表达式 map reduce filter
         map, filter在返回列表，需要 list函数输出列表 ******

lambda:
    lambda parameter_list: expression      :后面必须是表达式
    算子

三元表达式：条件为真时返回的结果 if 条件 else 条件为假时返回的结果

map: map(function, *iterables)，map的输出通过list()函数导出，可以优化代码，但没有提高代码效率  ******

reduce：处于 functools包中, reduce(function, sequence[, initial]) 
        连续计算：连续调用函数，最后返回一个数值或字符串    ******
        必须传入2个元素
        初始调用列表前两个元素，依次把接下来的列表元素做为reduce所需的参数，只输出一个值
        第二个列表参数位值可以不出现，此时初始值默认取第一个列表的前连个元素
        第二个列表参数可以使任意类型列表，字符串，数字等 ******
大数据中，map/reduce 是一种编程模型，map即是映射，reduce是归约， 主要用于并行计算 ******

filter：可以判断真假1，0  过滤器
        判断大小写等



"""

#匿名函数
def add(x,y):
    return x + y

f = lambda x,y: x+y  # 匿名函数， ：后面必须是lambda表达式
print(f(1,2))

x1 = 1
y1 = 2
r = x1 if x1 > y1 else y1  # 三元表达式
print(r)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# map函数
list_x = [1,2,3,4,5,6]
list_y = [9,8,7]
def  s(x):
    return x * x

r = map(s, list_x) # map(func, *iterables)
print('map函数: ',list(r)) # list导出map 结果

r2 = map(lambda x,y: x * x, list_x, list_y) # map通过匿名函数表达，可以传入多个list
print('map通过lambda表示：', list(r2)) # 多个列表同时传入时，list 传出较小的list
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# reduce: 连续计算
from functools import reduce
list_x2 = ['1','2','3']
r3 = reduce(lambda x,y: x * y, list_x, 'a') # reduce 连续调用lambda
                                            # 第二个列表参数位值可以不出现，此时初始值默认取第一个列表的前连个元素
                                            # 第二个列表参数可以使任意类型列表，字符串，数字等
r4 = reduce(lambda x,y: x + y, list_x2, 'a')

print(r3)
print(len(r3)) # r3有720位
print(r4)
print(len(r4))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# filter:
list_f = [1,2,3,4,5]
list_f2 = ['1','a','B','c']
r5 = filter(lambda x: x, list_f)
r6 = filter(lambda x: x, list_f2)
# r6 = filter(lambda x: x, list_x, list_f2)

print(r5)
print(list(r5))
print(list(r6))
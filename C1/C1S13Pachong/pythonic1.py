# 字典代替switch：字典映射，字典中通过函数代替字典中的value

# 列表推导式（集合推导式），map filter 
a = [1,2,3,4,5,6,7]
a2 = {1,2,3,4,5,6,7}
b = [i*i+ i**3 for i in a if i>=3] # 表达式-推导式-条件
b2 = [i*i+ i**3 for i in a if i>=3] # 通过列表对字典执行表达式推导后输出仍是列表
b3 = {i*i+ i**3 for i in a if i>=3} # 字典化，元组仍可以推导，输出对应结果
print(b)
print(b2)




import numpy as np 

a = np.arange(1, 21, 2) # 1~ <10，间隔为2
a1 = np.arange(10)
a2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
a3 = a2.astype(float)
a4 = a.reshape((((2,5)))) # 多个括号一个效果
a5 = a1.reshape(2,5) # .size  .ndim .zero .ones .random
a6 = np.ones((2,3,4), dtype=np.int32) # 初始化为1的矩阵，数据类型为int32
a7 = np.random.random((2,3))

print(a)
print(a4)
print(a5)

print('矩阵数组a2的维度：',a2.shape) # a2.shape查看矩阵数组的维度
print('矩阵a2的数据类型：',a2.dtype)  # dtype 数据类型
print('矩阵a2的转换数据类型：',a3) # astype

print('行求和：',a2.sum(axis=1))
print('列求和：',a2.sum(axis=0))
print('random：',a7)


b = (a == 5)
print(b)
print(a[b])  # 通过bool类型返回索引， 同样可以使用条件判断语句返回索引



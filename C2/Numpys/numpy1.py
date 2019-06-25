import numpy as np
from numpy import pi

a = np.arange(1, 21, 2) # 1~ <10，间隔为2
a1 = np.arange(10)
a2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
a3 = a2.astype(float)

a4 = a.reshape((((2,5)))) # 多个括号一个效果
a1.shape = (2,5) # shape直接修改了a1的形状
a5 = a1.reshape(2,5) # .size  .ndim .zero .ones .random
a10 = a1.reshape(5, -1) # reshape不修改a1形状， shape直接修改了a1形状 ****** 
                        # -1表示自动确定另一个维度 ******

a6 = np.ones((2,3,4), dtype=np.int32) # 初始化为1的矩阵，数据类型为int32
a7 = np.random.random((2,3))  # 两次括号表示产生2行3列矩阵， random区间 -1 ~1
a8 = np.linspace(0, 2*pi, 10) # 100个数，区间 0~2pi
a9 = (a == 5)


print(a)
print(a4)
print(a5)
print('a10: ', a10)

print('矩阵数组a2的维度：',a2.shape) # a2.shape查看矩阵数组的维度
print('矩阵a2的数据类型：',a2.dtype)  # dtype 数据类型
print('矩阵a2的转换数据类型：',a3) # astype

print('行求和：',a2.sum(axis=1))
print('列求和：',a2.sum(axis=0))
print('random：',a7)
print('linspace：',a8)
print(a9)
print(a[a9])  # 通过bool类型返回索引， 同样可以使用条件判断语句返回索引

print('ravel拉平矩阵:',a2.ravel()) # ravel 把矩阵换成向量，拉平矩阵
print('shape直接修改矩阵，a1.shape = (2,5):', a1) # 直接修改了a1的形状

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 矩阵乘法
print('矩阵乘法：') 
b1 = np.array([[1,1],[0,1]])
b2 = np.array([[2,0],[3,4]])

print('b1*b2：', b1 * b2) # 相同矩阵对应位置元素相乘
print('矩阵乘法2种形式: ', b1.dot(b2)) # 矩阵乘法2种形式
print('矩阵乘法: ', np.dot(b1, b2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 矩阵拼接
print('矩阵拼接：')
c1 = np.floor(10*np.random.random((2,2)))
c2 = np.floor(10*np.random.random((2,2)))
c3 = np.hstack((c1,c2))
c4 = np.vstack((c1,c2))

c5 = np.hsplit(c3, 2)
c6 = np.vsplit(c3, 2)

c7 = np.hsplit(c3, (2,3)) # 指定在c3第2列和第3列处切割，也可以使用矩阵 ******
c8 = np.hsplit(c3, np.array([2,3]))

print(c1)
print('hstack:', c3) # 横向拼接
print('vstack:', c4) # 纵向
print('~~~~~~~~~~~')

# 切割矩阵：
print('切割矩阵：')
print('hsplit:', c5)
print('vsplit:', c6)
print('指定矩阵切割1：', c7)
print('指定矩阵切割2：', c8)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



'''
numpy: 进阶

'''
import numpy as np 


# ndarray.dtype 元素类型  # dtype 默认float
# ndarray.shape 数组结构   ndim size itemsize flags数组内存信息 real imag data数组元素实际存储区
# ndarray.astype()修改元素类型
# ndarray.reshape()重新定义数组结构

# np.array() np.zeros  np.empty  np.ones  
np.eye(4, 5, k=-1) # 对角矩阵, k=-1表示偏移对角向下移1格
np.random.random(3)
a = np.random.randint(4, 5, size=(2, 3)) # zise= 可省略不写
print(a)

# 数值范围内创建数组
np.arange()
np.linspace(2, 10, num=100, endpoint=False) # num= 可省略不写，表示区间内均分取num个点数, 结束点默认True 
np.logspace() # log坐标

# 已有数组创建数组
np.asarray(a) 
np.empty_like()
np.zeros_like()
np.ones_like()

# 重复
a2 = np.range(3)
np.tile(a2, (2,3)) # 重复数组a2， (2,3)次
a3 = a2.repeat(2) # 重复每个元素2次

# 网格化
np.meshgrid()
np.mgrid[1:10:2, 2:11:2] # np.mgrid[]指定范围分割实现网格化，前后切片分别按照行和列实现网格化

# 包含虚数 ******
complex(2,5) # = 2 + 5i

# 数组操作
a4 = np.arange(9)


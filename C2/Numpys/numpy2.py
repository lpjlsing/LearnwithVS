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
np.linspace()
np.logspace()

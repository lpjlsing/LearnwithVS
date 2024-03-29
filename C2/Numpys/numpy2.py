'''
numpy: 进阶

pyhton数组 VS. numpy数组

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
a4[-1] # 最后一个元素
a4[2:5]
a4[:7:3] # 3表示步长
a4[::-1] # 逆序数组 ******
a4[:,:,1:3] # 所有的第2到4列(这里是1:3表示2到4列)，不包括第4列 ******

a5 = np.arange(24).reshape(2,3,4) # 2组3行4列
a5[1,2,3]
a5[0,:,:] # 等价于a[0], 或a[0,...] ******
a5[:,:,1:3] # 所有数组元素的2到4列且不包括第4列 ******
a5[1,:,-1] # -1表示最后一个元素，这句是第2组中每一排最后一个元素

# 
a6 = np.array([[1,2,3],[4,5,6]])
a6.ravel() # 返回一维数组
a6.rezise() # resize直接更改了原数组a6，而reshape不改变原矩阵 ******

a9 = np.rollaxis(a5, 2, 1)  # rollaxis: a5中换第3个轴移到第2个位置，其他轴相对顺序改变

a10 = np.rollaxis(a5, 1, 2) 
a11 = np.moveaxis(a5, 1, 2)  # moveaxis(a, source, destination)， 和rollaxis位置有所区别
a10.max(axis=0) # 每列最大输出为一行
a10.max(axis=1) # 每行最大输出为一列

# 数组合并和拆分 ******
# stack : 只出入一个tup类型, Join a sequence of arrays along a new axis. vstack : Stack along first axis. hstack : Stack along second axis. concatenate : Join a sequence of arrays along an existing axis
np.append(a9, a11, axis=0)  # 合并数组，使a11第1个轴到a9第1行。axis默认为flatten形式合并，axis=1表示ndarray 的第二个轴，这里 np.shape(a9)=(2,4,3)，第二个轴为4
np.concatenate(a9, a11) # 合并数组到一个元组
# np.hstack() np.vstack np.dstack # dstack至少3个轴, 在第三个轴stack ******
x, y, z = np.hsplit(a, 3) # 3表示拆分为3组数组需同时传入三个接受数组x,y,z
                          # hsplit(ary, indices_or_sections)

# 数组排序
np.sort() # sort(a, axis=-1, kind='quicksort/mergesort/heapsort', order=None)
np.argsort() # argsort(a, axis=-1, kind='quicksort', order=None)
             # 返回索引值

# 查找
np.argmax(a10, axis=1, out=None) # 返回索引值
np.nonzero(a10)
np.where(a < 4, a, a*10) 

# 增删元素
np.insert # insert(arr, (int, slice or sequence of ints Object), values, axis=None) , axis不指定则插入后输出flatten lsit
np.delete # delete(arr, obj, axis=None)
np.unique # 去重，unique(ar, return_index=False旧列表位置, return_inverse=False新列表位置, return_counts=False, axis=None)
          # unique会展开数组至一维结构

# IO：
# 二进制文件格式binary
np.save(file, Array data to be saved, allow_pickle=True, fix_imports=True) # pickle操作file之前先对对象进行序列化或反序列化，.npy
np.savez(file, *arr, **kwds) # 保存多个数组写入进文件，保存为原始未压缩二进制文件, .npz
np.load() # save, load, 貌似现在不使用 pickle 办法了 ******
# 文本txt
np.savetxt('name', a10) # 保存文本格式，loadtxt
# CSV
 
# 函数
np.around(a10, decimals)
np.floor(a10) # 去尾
np.ceil(a10) # 进一
np.sum 
np.nansum # 
np.cumsum # 指定轴求累进和
np.prod # 积
np.diff # 差
np.ptp # 最大差值
np.var # 方差
np.std # 标准差
np.median # 中位数
np.mean # 平均值
np.average # 加权平均 average(a, axis=None, weights=None, returned=False)



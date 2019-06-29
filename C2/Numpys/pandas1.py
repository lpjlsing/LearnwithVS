 """  
 pandas

 """

from pandas import pandas as pd
from numpy import numpy as np

#数据读取
a = pandas.read_csv("test")
a1 = a.head(3) # 默认read前5条数据，
a2 = a.tail(4) # 后四行
a3 = a.columns # 每个列的列名
a4 = a.shape 

a5 = a.loc[0,'ww'] # 取出第一行数据(位置为[0]),元素为'ww'的列
a6 = a.loc[3：6] # 取出第3-6行数据
a7 = a["aaa"] # aaa为列名，通过列名来定位对应的列，aaa可以使列表    ******

a8 = a.columns.tolist() # tolist定位到列名
c = a8.endswith('tt') # endswith，以tt为结尾的列名的元素
c1 = []
c1.append(c)

# 数据操作
b = a['aa']/100 
b1 = a['cc1'] * a['cc2'] # 列相乘，也可以做其他操作
a['new column'] = new_columns # 直接加入新的列到a中
max_columns = a['sd'].max() # max

# 排序数据
a.sort_values('aaaa', inplace=True, ascending=False) #默认从小到大、升序排序，缺失值一直放在最后
a.sort_index # sort_values, sort_index ******
a.reset_index(drop=True)  # reset_index 给索引值排序


c1 = a.isnull(asd) # isnull判断asd是否是空, 找出所有的空值到c1中 ******

sum(a['aas'])/len(a['aas'])， a['qqq'].mean() # 求平均值


# pivot_table
d1 = a(index='a1', value=['a2','a3'], aggfunc=np.mean or np.sum)  # a1为统计的基准， 和a1比较值为a2的关系np.mean， aggfunc默认为求均值 ******

# dropna
e1 = a.dropna(axis=0, subset['as1','as2']) # 丢掉对应值，dropna。 axis表示维度，找subset列中的值，然后丢掉

#apply
f1 = a.loc[250]
a.apply(f1, axis=1) # 返回第251行，第1（axis）列，数据 ******



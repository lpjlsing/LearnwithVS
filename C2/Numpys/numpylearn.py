#!/usr/bin/env python
# coding: utf-8


# In[1]:


import numpy as np
a = np.eye(4, 5, k=-1) #
a


# In[2]:


np.linspace(2, 10, num=7, endpoint=False) # 结束点默认True 


# In[3]:


np.logspace(2, 10, num=5) 


# In[4]:


a1 = np.random.randint(0, 9, size=(2, 3))
np.asarray(a1)


# In[5]:


# np.meshgrid()
nx, ny = (3, 2) 
x = np.linspace(0, 1, nx) 
y = np.linspace(0, 1, ny) 
xv, yv = np.meshgrid(x, y) 


# In[6]:


xv
yv
xv,yv


# In[7]:


# np.mgrid[]指定范围分割实现网格化
a2, a3 = np.mgrid[1:10:2, 2:11:2]
a2
a3
a2,a3


# In[8]:


a3


# In[9]:


# 数组操作
a4 = np.arange(9)
a5 = a4[::-1] # 逆序数组


# In[10]:


a5


# In[11]:


a5 = np.arange(24).reshape(2,3,4) # 2组3行4列
a5


# In[12]:


a5[1,2,3]


# In[13]:


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a6 = np.array([[1,2,3],[4,5,6]])
a6.ravel() # 返回一维数组


# In[14]:


a6


# In[15]:


a6.transpose() #转置行变列


# In[16]:


a6.resize((3,2))


# In[17]:


a7 = a6.resize(3,2) # resize更改了原矩阵，reshape不更改原矩阵


# In[18]:


a7 = a6.resize((3,2))


# In[19]:


a6


# In[20]:


a7


# In[21]:


np.shape(a7)


# In[22]:


np.shape(a6)


# In[23]:


a5


# In[24]:


a9 = np.rollaxis(a5, 2, 1)  # a5中换第3个轴移到第2个位置，其他轴相对顺序改变


# In[25]:


a9


# In[26]:


a10 = np.rollaxis(a5, 1, 2)
a11 = np.moveaxis(a5, 1, 2) # 和a9一样


# In[27]:


a10


# In[28]:


a11


# In[29]:


# 合并数组
np.append(a9,a11,axis=0)


# In[30]:


np.append(a9,a11,axis=1)


# In[31]:


np.append(a9,a11)


# In[32]:


np.append(a9,a11,axis=2)


# In[33]:


np.shape(np.append(a9,a11,axis=0))


# In[34]:


np.shape(np.append(a9,a11,axis=1))


# In[35]:


np.shape(np.append(a9,a11,axis=2))


# In[36]:


a12 = np.array((1,2,3)) 
a13 = np.array((2,3,4)) 
np.dstack((a12,a13)) 


# In[37]:


np.shape(a12)


# In[38]:


np.shape(np.array([[1],[2],[3]]))


# In[39]:


np.shape(np.dstack((a12,a13)) )


# In[40]:


a14 = a9 * 10
a14


# In[41]:


a15 = np.append(a9,a11,axis=0)
a16 = np.append(a9,a11,axis=1)
a17 = np.append(a9,a11,axis=2)


# In[42]:


a15
a16
a17


# In[43]:


# stack : 只出入一个tup类型数据
np.vstack((a14,a15))


# In[44]:


np.hstack((a14,a16))


# In[47]:


np.dstack((a14,a17))


# In[53]:


a18 = np.arange(9).reshape(3,3)
a19 = np.arange(9,18).reshape(3,3)
np.hstack((a18,a19))


# In[54]:


np.shape(a18)


# In[55]:


np.shape(np.dstack((a18,a19)))


# In[ ]:


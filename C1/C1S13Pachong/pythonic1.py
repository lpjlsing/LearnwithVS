# 字典代替switch：字典映射，字典中通过函数代替字典中的value

# 列表推导式（集合推导式），map filter 
a = [1,2,3,4,5,6,7]
a2 = {1,2,3,4,5,6,7}
b = [i*i+ i**3 for i in a if i>=3] # 表达式-推导式-条件
b2 = [i*i+ i**3 for i in a if i>=3] # 通过列表对字典执行表达式推导后输出仍是列表
b3 = {i*i+ i**3 for i in a if i>=3} # 字典化，元组仍可以推导，输出对应结果  ******
print(b)
print(b2)

# 对字典表达式推导，需注意key,value是可能需要两个参数
# 元组要注意元组的不可变性


# None: 本身是个对象，NoneType
# None 为tpye类型，表示不存在；False为bool类型，表示真假
c1 = ''
c2 = []
c3 = False
c4 = None

if not a: # not判断a是True or False
if a is None: # is做判断，a 是否和None是一样
if a:
if None: # None只对应False

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
class D():
    def __len__(self):
        return 0  # (True)
    
    def __bool__(self):
        return False 

d = D()

bool(None)
bool([])
bool(D)
if D:    # 对于自定义对象，其值True or False 跟自定义的对象有关
         # D的真假跟定义的class内部方法相关，而不是只要D存在就一定是真 ******
    print('T')
else:
    print('F')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 在列表头部操作多的场景使用 deque：
#  模块列表是基于数组结构（Array）实现的，
# 当你在列表的头部插入新成员（list.insert(0, item)）时，它后面的所有其他成员
# 都需要被移动，操作的时间复杂度是 O(n)。这导致在列表的头部插入成员远比在尾部追
# 加（list.append(item) 时间复杂度为 O(1)）要慢。
# 如果你的代码需要执行很多次这类操作，请考虑使用 collections.deque 类型来替代列表。
# 因为 deque 是基于双端队列实现的，无论是在头部还是尾部追加元素，时间复杂度都是 O(1)。

# 当需要判断成员是否存在于某个容器时，用集合比列表：
# item in [...] 操作的时间复杂度是 O(n)，而 item in {...} 的时间复杂度是 O(1)
# 字典与集合都是基于哈希表（Hash Table）数据结构

# 每个内置容器类型，其实就是满足了多个接口定义的组合实体

# python面向接口而非具体实现来编程 ******

# 动态解包:
# 是指使用 * 或 ** 运算符将可迭代对象“解开”
# user = {**{"name": "piglei"}, **{"movies": ["Fight Club"]}} 


# next():
# 是一个非常实用的内建函数，它接收一个迭代器作为参数，然后返回该迭代器的下一个元素。
# 使用它配合生成器表达式，可以高效的实现“*从列表中查找第一个满足条件的成员”*之类的需求。
numbers = [3, 7, 8, 2, 21]
# 获取并 **立即返回** 列表里的第一个偶数
print(next(i for i in numbers if i % 2 == 0))


# 有序字典来去重:
l = [10, 2, 3, 21, 10, 3]
from collections import OrderedDict  # 有序字典
l1 = list(OrderedDict.fromkeys(l).keys())
print(l1)


# 枯竭的迭代器:  生成器表达式、map、filter 等内建函数  ******
# 完整遍历过它们后，之后的重复遍历就不能拿到任何新内容

# 别在循环体内修改被迭代对象：
# 使用一个新的空列表保存结果，或者利用 yield 返回一个生成器
def remove_even(numbers):
    """去掉列表里所有的偶数
    """
    for i, number in enumerate(numbers):
        if number % 2 == 0:
            # 有问题的代码
            del numbers[i]

numbers = [1, 2, 7, 4, 8, 11]
remove_even(numbers)
print(numbers)
# OUTPUT: [1, 7, 8, 11]


# 异常：
# with语句在打开文件后会自动调用finally中的关闭文件操作
# finally 可以用来释放资源

# for语句本身会处理StopIteration异常

# 需要访问一个不确定的属性： 
# a = getattr(func, 'name', 'default')
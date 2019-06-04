# ctrl + c 可以强制停止死循环程序
a = 1

while a <= 10: 
    a += 1
    print(a)
else:
    print('EOF')

# for 循环主要用来 遍历/循环 序列或集合、字典
a = [['1a', '2b', '3c'], [1,2,3]]
for x in a: # 集合被打印出来
    print(x)

for x in a:
    for y in x: # 通过这种嵌套来实现集合中的元素分别打印出来
        print (y, end='\n') # '\n'为 换行
else:
    print('hehe')

for x in a:
    if x == 2:
        break # continue表示这个 2 不会被输出而继续下一个循环， 
              # 而break则直接结束内部循环，且不执行内部的else，但外部循环并不被结束
else:
    print('hehe')

for y in range(0,10): # 0，第一个参数为开始数字。10，第二个餐宿为可改变的数量， range 函数
    print(y)

for y in range(0,10,2):
    print(y, end='！')



    
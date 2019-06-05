for y in range(0,10): # 0，第一个参数为开始数字。10，第二个参数为可改变的数量， range 函数
    print(y)

for y in range(0,10,2): # 步长为 2，打印出 偶数
    print(y, end='！')

a = [1,2,3,4,5,6,7,8,9,0]

for i in range(0, len(a), 2): #打印出 奇数
    print(a[i], end='!')

b = a[0:len(a):2] #切片去元素， 同样可以实现只打印奇数，可以代替 for 循环

print(b) 

c = 110


    
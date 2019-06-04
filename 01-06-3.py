'''
snippet片段快速coding

'''
# snippet 片段 ******

# if condition:
#     pass
# else:
#     pass

a = True

if a:
    pass # 使用 tab 可以直接从 a: 处调到 条件 pass 位置
         # pass #空/站位语句
         # 代码块 # 嵌套代码块不要超过3层

if True:
    pass

if False:
    pass    

b = input()  
b = int(b) # 说明 b 的类型
print('b is ', b) # 不能使用中文符号
if b == 1:
     print('aa')
elif b == 2: # elif需配合 if 才能使用，python没有 switch 或者 case， 
             # 可以使用 elif 或字典来代替使用
    print('bb')
elif b == 3:
    print('cc')

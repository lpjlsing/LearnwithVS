'''
    开头写模块注释
    包- 模块- 类- 函数、变量(类的本身特性)
'''
print ('hello, 1st')  # 

mood = True 

a = 1
b = 0
a or b # 直接判断不同量之间关系

ACCOUNT = 'woshishui'  # constant（常量）需要大写命名， 如 ACCOUNT
PASSWORD = '123456'

print('account:')
user_account = input()  # pylink认为只在函数、类中多函数命名视为常量

print('password:')
user_password = input() 

if ACCOUNT == user_account and PASSWORD == user_password: 
#语法标识前面不允许有空格，比如这里的‘：’
    print('success' ) # 4个空格为一个缩进 
else:
    print('fail') # 程序末尾需留一行空行
    



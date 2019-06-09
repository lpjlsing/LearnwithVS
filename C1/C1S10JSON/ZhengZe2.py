""" 
正则表达式

re.sub实现函数替换 
re.search
re.match

分组：group()函数：可以传递一个参数，指定获取的组号，默认为0
                  group(0)返回的是完整的匹配结果，跟有多少个组无关

"""
import re

s = 'ABC345629867396dGainWHAT'
s1 = 'ABC345629867396dGainWHAT'

def convert(value):
    matched = value.group() 
    if int(matched) >= 6: # 需要先把字符数字转换为整数数字
        return '9' # 这里的输出应该符合所调用的规则，在正则中必须是字符串而不是数字9
    else: 
        return '0'

r = re.sub('\d', convert, s)
print(r)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# re.search， match
print('其它正则表达式函数：')
s2 = re.match('\d',s1) # match从字符串首字母匹配，如果没有符合的字符串将返回为空
print(s2)
s3 = re.search('\d',s1)
print(s3)
print(s3.group())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#分组group方法
print('~~~~~~~~~匹配字符串中间的部分：')
life = 'life is short, I use python, I love python'
life1 = re.search('life.*python',life) # * 前面的字符串处\n外全部匹配
life2 = re.search('life(.*)python',life)
life3 = re.search('life(.*)python(.*)python',life) 
life4 = re.findall('life(.*)python',life) 

print('search仍包括用于匹配的字符：没有()组')
print(life1.group()) # 这里匹配出了包括用于匹配字符的字符life和python
                     # group(0)返回的是完整的匹配结果，跟有多少个组无关
print('search通过group匹配指定位置字符串；返回字符串，多个组时同时返回时返回 元组')
print(life3.group(0,1,2)) # group(0)返回的是完整的匹配结果，跟有多少个组无关
print(life3.groups())     # 只返回组之间的字符串 元组
print('findall通过group匹配指定位置字符串：返回 列表')
print(life4) #匹配指定的第一个字符串组
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')






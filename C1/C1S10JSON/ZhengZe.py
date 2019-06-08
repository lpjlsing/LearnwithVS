""" 
正则表达式： 特殊的字符序列，，可以检测与我们的设定是否一致相匹配
    检查
    检索：快速检索文本，实现文本的一些
    替换文本

字符集：一组re构成普通字符，'\d'是元字符，匹配单一字母或字符
概括字符集：  '\d' = '[0-9]'，\d即是一个概括集， 匹配单一字符，比如一个数字或字母
单词字符：\w匹配单词字符，[\w] = [Aa-Zz,0-9,_] (下划线,空格，回车等也算单词字符)
空白字符：\s

数量词：｛3，6｝，最小3最大6个字符，表示以此取出的字符串数量
        贪婪 和非贪婪：python默认贪婪模式， {3,6}? --> ？使数量词匹配时为非贪婪
        * 表示前面的字符匹配 0次 或 无限次
        + 匹配 1次 或 无限多次，无限指匹配到字符后继续去字符的位数 ******
        ? 匹配 0次 或 1次        
        可以对字符串直接进行贪婪操作，如 s7

边界匹配：


 """

import re # regular expression，导入正则表达式包

# 正则表达式
a = 'c|b|d|e|f|python1' # |表示按元素逐个取 或 操作，||表示取到第一个元素时停止取或
                        # or 则按整体对象去或操作
print(a.index('python1')>-1)

r = re.findall('python1',a)  # findall 以列表返回
print(r)

if len(r) > 0:
    print('Including python1')
else: 
    print('0')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('~提取出字符串中的所有数字：1. for循环   2.re')
b = '56473n28mz1m98d4b67r 365n48c3xm'
c = re.findall('3',b)
print(c)
print('~通过 元字符\d 使用 普通字符re 打印出所有的数字: ')
d = re.findall('\d',b) # \d 表示一个数字字符 0-9 
e = re.findall('\D',b) # \D 则取出一个非数字字符
print(d)
print(e)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('~通过re取出特定目标字符：')
letters = 'abc,aec,acc,bbc,aec,aff,acf'
letter1 =re.findall('a[ef]f',letters) # []中间表示在'a_f'中间的字符，ef为'或'关系
letter2 =re.findall('a[^ef]f',letters) # ^ 表示都 不是 ef的字符
letter3 =re.findall('a[b-f]f',letters) # - 表示 b-f中间 的所有字符
print('letter1：',letter1)
print('letter2：',letter2)
print('letter3：',letter3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 字符集
print('同时输出字符和数字：') # 
f = '111\1n3n4n 55d\ds\tr\ntnt\rsg%&b\brv__v76' 
f1 = re.findall('\w',f) # \w 匹配 单词字符, Aa-Zz,0-9,_ (下划线,空格，回车等也算单词字符)
print(f1)
f2 = re.findall('[A-Za-z0-9]',f)
print(f2)
f3 = re.findall('\s',f) # 空白字符,如 空格 \t \r \n
print(f3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 数量词
print('数量词与贪婪和非贪婪 {3,6}?')
s = 'pytho1111java678phppython1pythonn2pythonnn3'
s1 = re.findall('[a-z]{3}',s) # {3，6}: 字符串最小3个最大6个字符，表示取出的字符串数量
print(s1)
s2 = re.findall('[a-z]{3,6}',s) # 贪婪匹配， 区间：3-6，此时3为非贪婪，6为贪婪模式 
print(s2)
s3 = re.findall('[a-z]{3,6}?',s) # 贪婪匹配， 区间：3-6
print(s3)
s4 = re.findall('python*',s) # * 表示它前面的字符 0 次 或 无限次 匹配
s5 = re.findall('python+',s)
s6 = re.findall('python?',s)
print(s4) 
print(s5)
print(s6)
s7 = re.findall('python{1,2}?',s) # 可以直接对字符串进行贪婪操作，此时非贪婪取最下值
print(s7)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 边界匹配
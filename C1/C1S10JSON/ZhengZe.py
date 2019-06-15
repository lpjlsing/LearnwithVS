""" 
正则表达式： 特殊的字符序列，，可以检测与我们的设定是否一致相匹配
    检查
    检索：快速检索文本，实现文本的一些
    替换文本
    输出结果为列表

re.findall: 查找， 返回 列表， 而search中group返回 元组
re.sub: 替换
re.match: 首字母开始匹配
re.search: 搜索整个字符串，找到第一个符合的字符串后返回，一次返回第一个出现的匹配字符串
re,span：返回匹配到的字符串的位置

字符集：一组re构成普通字符，'\d'是元字符，匹配单一字母或字符
概括字符集：  '\d' = '[0-9]'，\d即是一个概括集， 匹配单一字符，比如一个数字或字母
单词字符：\w 匹配单词字符，不包括空格等字符，[\w] = [Aa-Zz,0-9,_] (下划线,空格，回车等也算单词字符)
空白字符：\s  
     . : 匹配换行符\n之外的其它所有字符     
        
数量词：
        'str{3}'--> 字符串连续重复3次的取出
        '[str]{3}'--> 字符串连续有3个字符的取出
       ｛3，6｝，最小3'最大6个字符，表示以此取出的字符串数量
        贪婪 和非贪婪：python默认贪婪模式， {3,6}? --> ？使数量词匹配时为非贪婪
        * 表示前面的字符匹配 0次 或 无限次   
        + 匹配 1次 或 无限多次，无限指匹配到字符后继续去字符的位数 ******
        ? 匹配 0次 或 1次        
        可以对字符串直接进行贪婪操作，如 s7

边界匹配：'^\d{4,8}$'--> '^ ... $'即表示边界匹配，可以实现完整的匹配
         ^ : 字符串开始标志，属于 占位符
         $ : 字符串末尾的标志，001$表示以001结束的字符串

组： (str), 表示一组字符串，表示 且 关系，需同时满足。而[str]表示单个字符间的 或 关系
     ()和 group 匹配
     groups() 只返回组之间的字符串

匹配模式： re的第三个关键字， re.I: 忽略大小写(flags) ******
          re.S: 符号将匹配所有字符，包括 \n 
          不同匹配模式之间通过 | 符号连接
          
替换： re.sub --> # 0: 匹配讲无限制替换下去，即只要有 C# 将被替换为 Go
            # 1： 只替换第一个
           动态替换：可以替换为函数。可以通过把函数当成参数，动态的替换字符串 ******
      re.replace --> 字符串本身不可变，如要替换操作，需重新生成字符串然后替换

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
print('~~~~~~~~~~~~~~~~')

print('~提取出字符串中的所有数字：1. for循环   2.re')
b = '56473n28mz1m98d4b67r 365n48c3xm'
c = re.findall('3',b)
print(c)
print('~通过 元字符\d 使用 普通字符re 打印出所有的数字: ')
d = re.findall('\d',b) # \d 表示一个数字字符 0-9 
e = re.findall('\D',b) # \D 则取出一个非数字字符
print(d)
print(e)
print('~~~~~~~~~~~~~~~~')

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

# 边界匹配：'^\d{4,8}$'--> '^ ... $'即表示边界匹配，可以实现完整的匹配
print('边界匹配')
bd = '100001'
bd1 = re.findall('^\d{3,8}$',bd)
bd2 = re.findall('^100',bd) # 100开始的字符串
bd3 = re.findall('100$',bd) # 100结束的字符串
print(bd1)
print(bd2)
print(bd3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 组
z = 'abcabcabcabcabcabc'
z1 = re.findall('(abc){2}',z) # (str) 即表示一组字符串的 且 关系
print(z1)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 匹配模式：大小写，替换。。。
print('匹配模式: ')
l = 'PythonC#TavaPHPC#Tensorflow'
l1 = re.findall('c#.{2}', l, re.I) # re.I 表示忽略大小写, 默认为全是大写输出
l2 = re.findall('c#.{1}', l, re.I | re.S) # re.S 表示符号将匹配所有字符，包括 \n
                                          # 这里的 | 表示 且 关系
                                          # c#.{1}中的 . 表示它前面的字符串#后面还可再取{1}位字符
l3 = re.findall('P.{1}', l, re.I | re.S)                                          
print('l1 = ',l1) 
print('l2 = ',l2) 
print(l3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# re替换和动态替换
print('re动态替换：')
l4 = re.sub('C#','Go',l,0) # 0: 匹配讲无限制替换下去，即只要有 C# 将被替换为 Go
                           # 1： 只替换第一个
                           # re.sub 可以替换为一个函数，返回一个对象 ******
# l5 = re.replace('C#','Go') # 
print('~~~~~~re.sub替换字符串为函数：')
def convert(value):
    matchced = value.group() # 把对象value通过group方法存入matched 
    print(value) # re.sub返回函数中的对象
    return '00' + matchced + '99' 
l6 = re.sub('C#', convert, l) # 当函数对象value传入使用matched, 格式为 (str,def,l6)
                              # C#此时被 动态 替换
print(l6)


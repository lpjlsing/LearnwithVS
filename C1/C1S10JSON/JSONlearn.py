"""
JavaScript Object Notation 对象标记    

JS只是实现ECMASCRIPT标准之一，这种是实现还有ActionScript

JSON：只是一种轻量级的数据的交换格式，为中间数据类型。 XML：大量级数据
      有自己的数据类型
      REST服务的标准格式，服务器相关  
JSON字符串：字符串是JSON的表现形式，符合格式的字符串即为JSON字符串
JSON对象： python中没有这种说法，是JS中说法

JSON在JS中表示对象，python中则为字典 ******

print(json.dumps(data, indent=2))  ******

相比于XML：
易阅读
易解析
网络传输效率高，传输数据少

跨语言交换数据 ******

JSON：网站后台--HTML,JSON--> 浏览器

反序列化：  字符串转换为某种数据结构
序列化过程：python数据转换为字符串 json.dumps()，接收一个对象

存储序列化后对象：NOSQL MongoDB

"""
import json

# JSON object array, json字符集合
json_str = '{"name": "lisa", "age": 27, "flag":false}' # json中字符串一定要加 '...' 来表示外部字符串
                                # python的bool类型输出: False，python中首字母大写
                                # "...."来表示内部字符串，python中json为一个字典
s = json.loads(json_str) #json导入
print(type(s)) # s类型为字典
print(s) 
print(s['name'])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 反序列化
s1 = [
    {"name": "lisa", "age": 27, "flag": False},
    {"name": "lisa2", "age": 27.2 },
    {"name": "lisa3", "age": 27.4, "flag": False},
    ] 

s3 = json.dumps(s1) #反序列化
print(type(s1)) #字典返回成了列表 
print(s1)


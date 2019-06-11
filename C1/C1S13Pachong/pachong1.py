""" 
爬虫

爬虫前奏： 
目的-网页-标签 

定位标签： 闭合性

根据http请求，向服务器发送，获取返回的http，最后用re提取所需数据
编码类型控制: strict，replace, errors='ignore'
乱码时，配置headers解决。https://blog.csdn.net/qq183837971/article/details/81631360

断点调试 F5 F10 F11


""" 

import re
from urllib import request
# import urllib3
 
# http = urllib3.PoolManager()
# r = http.request('GET', url)
# print(chardet.detect(r.data))
# print((r.data).decode('gb2312', 'ignore'))
# return (r.data).decode('gb2312', 'ignore')


class Spider():
    url = 'https://www.douyu.com/g_DOTA2'
    root_pattern = '<div class="DyListCover-content">([\s\S]*?)</div>'
        # 正则表达式来匹配的字符串定位标签
        # *：匹配一次货多次  ?: 非贪婪匹配

    def __fetch_content(self): # 私有方法 __fetch, 实例方法需要self
        r = request.urlopen(Spider.url) # 实例方法中读取url
        # response = request.get(url)
        # print(response.encoding)  # 输出url的编码类型
        htmls = r.read()  # bytes 
#        htmls.decode('utf-8','ignore')
        htmls = str(htmls, encoding='utf-8', errors='ignore') 
        # htmls = htmls.decode('utf-8')
        # htmls = str(htmls, encoding='utf-8')
                              # 
                              # 乱码时，配置headers解决。https://blog.csdn.net/qq183837971/article/details/81631360
        a = 1 # 测试用变量
        return htmls # 函数输出结果(这个不要忘记添加)

# htmls --> class="DyListCover-content": user 和 hot 的父级闭合标签
# class="DyListCover-user"
# class="DyListCover-hot"

    # 分析网址
    def __analysis(self, htmls):  # 分析调用的htmls
        root_html = re.findall(Spider.root_pattern, htmls)
 #       print(root_html[0])
        a = 1  # 调试变量

    # 入口函数
    def go(self):  # 公开方法，这里是入口方法
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()


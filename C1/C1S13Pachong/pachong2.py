""" 
爬虫

加入定时器

""" 

import datetime
import time
import re
from urllib import request
from threading import Timer # 定时器

# import requests
 
# http = urllib3.PoolManager()
# r = http.request('GET', url)
# print(chardet.detect(r.data))
# print((r.data).decode('gb2312', 'ignore'))
# return (r.data).decode('gb2312', 'ignore')


class Spider():
    url = 'https://www.huya.com/g/dota2'
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
        # 正则表达式来匹配的字符串定位标签
        # *：匹配一次或多次  ?: 非贪婪匹配

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
    def go(self):  # 公开方法，这里是入口函数
         # 记录该次爬取时间，为了便于后期的分析，开始爬取时记录当前的爬取时间作为该次爬取到的所有数据的爬取时间
        crawl_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 爬取时间
        print('Time is: ',crawl_start_time)
        htmls = self.__fetch_content()
        self.__analysis(htmls)
    #    # 定时器，定时半小时执行爬取程序，计算整个过程一次爬取时间，1800-爬取所用时间为间隔时长
    #     crawl_space_time = 86400 - (float(int(datetime.datetime.now().timestamp())) - time.mktime(time.strptime(crawl_start_time,'%Y-%m-%d %H:%M:%S')))
    #     # print("==========================================================================================")
    #     print("       爬取结束!等待下一次爬取,下一次爬取将于[" + str(crawl_space_time) + '] 秒后进行……      ')
    #     # print("==========================================================================================")
    #     t = Timer(crawl_space_time, Spider)
    #     t.start()
 
spider = Spider()
spider.go()


""" (模块注释)

类注释，方法注释

爬虫

加入定时器

精炼爬虫模块, 使数据更规范， stripe()函数

排序函数 __sort(): 
排序的时候必须制定排序类型 key , sorted(..., key = ..., reverse = True)
reverse
如果需要，把字符串转换成数字

展示函数 __show()， 这里在把数据传入数据库时可以通过更改这里实现  ******

BeautifulSoup  ******
 
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


class Spider(): # 爬取数据
    """ 
    类注释

    """
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
        # 正则表达式来匹配的字符串定位标签    
        # *：匹配一次或多次  ?: 非贪婪匹配    
    name_pattern = '<i class="nick" title=([\s\S]*?)</i>' # re 来定位名字
    hot_pattern = '<i class="js-num">([\s\S]*?)</i>' # 定位观看人数

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
        """  
        
        方法注释

        """
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = [] # 这个列表用于存储爬到的数据
        print(root_html[0])
        sum = 0
        print('Spider Finished Time: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        for html in root_html:  # 找出所有的相似标签
            name = re.findall(Spider.name_pattern, html)
            hot = re.findall(Spider.hot_pattern, html)
            anchor = {'name':name, 'hot':hot}  # 字典形式存储需要的数据类型
            anchors.append(anchor)  # 找到的字典信息添加到列表中
            sum += 1
#        a = 1  # 调试变量  
        # print(anchors) 输出列表完整内容
        print(anchors[0])
        print('当前总数：', sum)
        return anchors # 这个返回数据为列表

    def __refine(self, anchors): # 精炼得到的字典数据类型
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'hot':anchor['hot'][0]
            }
        return map(l, anchors) # map返回列表类型数据

    def __sort(self, anchors):  # 排序函数
        anchors = sorted(anchors, key = self.__sort_seed, reverse = True)  # 对获得的数据排序
        return anchors  # 
    
    def __sort_seed(self, anchor): # 
        r = re.findall('\d*', anchor['hot']) # 这里字符串通过re转成数字文本，*保证小数点后数字也导出来
        number = float(r[0]) # 文本换成数字，采用float类型数字
        if '万' in anchor['hot']: # 简写数字
            number *= 10000
        return number # 返回最终的数字结果

    def __show(self, anchors): # 展示函数，当传入数据库时，更改这里

         print('实时排名：')
         for rank in range(0, len(anchors)): # 打印排序结果
            print(str(rank + 1) + ':' 
            + anchors[rank]['name'] + '    ' 
            + anchors[rank]['hot']) 

    # 入口函数 
    def go(self):  # 公开方法，这里是入口函数
         # 记录该次爬取时间，为了便于后期的分析，开始爬取时记录当前的爬取时间作为该次爬取到的所有数据的爬取时间
        crawl_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 爬取时间
        print('Start Time : ',crawl_start_time)
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls) # 接受私有函数return值
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)  # 调用所需函数

        # print(anchors)        
        print('Anchors Finished Time: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #    # 定时器，定时半小时执行爬取程序，计算整个过程一次爬取时间，30S-爬取所用时间为间隔时长
    #     crawl_space_time = 30 - (float(int(datetime.datetime.now().timestamp())) - time.mktime(time.strptime(crawl_start_time,'%Y-%m-%d %H:%M:%S')))
    #     # print("==========================================================================================")
    #     print("       爬取结束!等待下一次爬取,下一次爬取将于[" + str(crawl_space_time) + '] 秒后进行……      ')
    #     # print("==========================================================================================")
    #     t = Timer(crawl_space_time, Spider)
    #     t.start()



spider = Spider()
spider.go()


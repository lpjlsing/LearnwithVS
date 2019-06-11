""" 
爬虫

爬虫前奏： 
目的-网页-标签 

根据http请求，向服务器发送，获取返回的http，最后用re提取所需数据

断电调试 F5 F10 F11


""" 
from urllib import request

class Spider():
    url = 'https://www.douyu.com/g_DOTA2'

    def __fetch__content(self): # 私有方法 __fetch__, 实例方法需要self
        r = request.urlopen(Spider.url) # 实例方法中读取url
        htmls = r.read()  # bytes 
        htmls = str(htmls, encoding='utf-8')
        a = 1

    def go(self):  # 公开方法，这里是入口方法
        self.__fetch__content()



spider = Spider()
spider.go()


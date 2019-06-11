from bs4 import BeautifulSoup
import urllib.request

def get_html(url):
    page = urllib.request.urlopen(url) 
    htmlcode = page.read().decode('utf-8') 	#改为gbk解码
    return htmlcode

url = 'https://www.douyu.com/g_DOTA2' 
html = get_html(url) 
soup = BeautifulSoup(html,'html.parser')  #使用html.parser

print(soup)

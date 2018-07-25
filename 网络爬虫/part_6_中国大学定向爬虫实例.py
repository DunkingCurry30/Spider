 ######################
 # 信息提取的一般方法 # 基于bs4库的html内容查找方法
 ######################

#find_all(name,attrs,recursive,string,**kwargs) 返回一个列表类型，存储查找的结果

 #name：对标签名称的检索字符串,可以为列表类型['a','b']，搜索多个标签

 #attrs：对标签属性值的检索字符串，可标注属性检索,这里是精确查找，模糊匹配需要正则表达式

 #recursive：是否对子孙全部搜索，默认为True

 #string：<>...</>中字符串区域的检索字符串

 #由于find_all极其常用,这里引入了两种简写形式：<tag>()和soup()，在括号中填入内容可以直接进行搜索

#find_all的7个扩展方法,其参数与find_all相同

 #find()：搜索且只返回一个结果，字符串类型
 #find_parents()：在先辈节点中搜索，返回列表类型
 #find_parent()：在先辈节点中返回一个结果，字符串类型
 #find_next_siblings()：在后续平行节点中搜索，返回列表类型
 #find_next_sibling()：在后续平行节点中返回一个结果，字符串类型
 #find_previous_siblings()：在前序节点中搜索，返回列表类型
 #find_previous_sibling()：在前序平行节点中返回一个结果，字符串类型

#中国大学排名定向爬虫实例

import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        print('出现异常')
        return ""

def fillUnivList(html):
    ulist = []
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
    return ulist

def printUnivList(ulist,num):
    #中文字符和英文字符占用字符不相等,这里使用中文空格(chr(12288))填充解决此问题
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format('排名','大学','地区','总分',chr(12288)))
    for i in range(num):
          u = ulist[i]
          print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
          
def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    ulist = fillUnivList(html)
    printUnivList(ulist,20)

main()
          

          
          










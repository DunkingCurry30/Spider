import requests
from bs4 import BeautifulSoup
import re
def getHTMLText(url):

    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        print('出现异常')


def findStockInfo(html):
    alist = []
    #查找股票信息
    pat = re.compile('>.*\(\d{6}\)')
    result = pat.findall(html)[700:710]
    for item in result:
        #分离股票信息和股票代码，存入infolist
        stock = item.split(">")[2]
        code = re.search(r'\d{6}',stock).group(0)
        name = stock.split('(')[0]
        alist.append([name,code])
    return alist

def findPrice(url,infolist):
    pricelist = []
    process = 1
    ls = len(infolist)
    for i in infolist:
        #进度条
        #print("{}/{}".format(process,ls))
        try:
            url_3 = url_2 + i[1]
            html = getHTMLText(url_3)
            soup = BeautifulSoup(html,'html.parser')
            price = soup.find('dd','s-up').string
            if price != "":
                pricelist.append(price)
                count += 1
        except:
            pass
        finally:
            process += 1
    return pricelist

def print(infolist,pricelist):
    print("{:8}\t{:8}]t{:6}".format("股票名称","股票代码","价格"))
    for stock,price in zip(infolist,pricelist):
        print("{:8}\t{:8}]t{:6}".format(stock[0],stock[1],price))
              
#从东方财富网获取股票代码及名称
url = 'http://quote.eastmoney.com/stock_list.html#sz'
html = getHTMLText(url)
infolist = findStockInfo(html)

#从百度获取对应股票的价格
url_2 = 'https://gupiao.baidu.com/stock/sh'
pricelist = findPrice(url_2,infolist)

print(infolist,pricelist)
    

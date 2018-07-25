import re
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        print('出现异常')
        return 0

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
        return ilt
    except:
        print("异常")
def printGoodsList(ilt):
    print("{:<6}\t{:<8}\t{:^16}".format("序号","价格","商品信息"))
    count = 1
    for g in ilt:
        print("{0:{3}<6}\t{1:{3}<8}\t{2:{3}^16}".format(count,g[0],g[1],chr(12288)))
        count += 1
def main():
    goods = '电脑'
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            print(url)
            html = getHTMLText(url)
            infolist = parsePage(infolist,html)
        except:
            continue
    printGoodsList(infolist)

main()

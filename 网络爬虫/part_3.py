#实例1：京东商品页面的爬取
import requests
'''
url = "https://item.jd.com/7629588.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('出现异常')
'''
#实例2：亚马逊商品页面的爬取
'''
url = 'https://www.amazon.cn/gp/navigation/ajax/dynamic-menu.html?wishlistItems=wishlist&metricKey=wishlistMetric&rid=FP07938MB2T3FK8RX7EH&isFullWidthPrime=0&isPrime=0&dynamicRequest=1&weblabs=&isFreshRegionAndCustomer=&primeMenuWidth=310&_=1532317700607'
#F12进入控制台->Network->headers->user-agent,获取可用的user-agent参数
kv = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
      +'537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('出现异常')
'''
#实例3：百度/360关键词提交

#百度的关键词接口：http://www.baidu.com/s?wd= keyword(对keyword进行替换来提交关键词)
#360的关键词接口：http://www.so.com/s?q= keyword(方法与上面类似)
'''
keyword = 'python'
kv = {'wd':keyword}
url = 'http://www.baidu.com/s'
try:
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
except:
    print('出现异常')
'''
#实例4 从网络爬取图片
import os
'''
url = 'https://www.bilibili.com/video/av27502739'
root = 'C:/Users/Administrator/Desktop/Python/网络爬虫/图片/' 
filename = root+url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(filename):
        r = requests.get(url)
        r.raise_for_status()
        with open(filename,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('文件获取失败')
'''
#实例5：IP地址归属地的自动查询
    
url = 'http://m.ip138.com/ip.asp'
ip = '183.64.61.21'
kv = {'ip':ip}
try:
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('出现异常')
#通过这个实例，可以发现我们在一个网站上可以先人工输入内容，查看网站地址的变化，以此来获
#得网站的api接口。










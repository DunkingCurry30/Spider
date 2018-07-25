
 #######################
 # 构建一个request对象 #
 #######################

#r = requests.get(url,params = None,**kwargs)
 
#r：response对象，代表网页链接返回的所有内容

#params:url中的额外参数，字典或字节流格式,optional

#**12个控制访问的参数

 ######################
 # Response对象的属性 #
 ######################

#r.status_code：http请求的返回状态,200表示连接成功,404(非200)表示连接失败

#r.text：http响应内容的字符串形式,即url对应的页面内容

#r.encoding：从http header中猜测的响应内容编码方式

#r.apparent_encoding：从内容中分析出的响应内容编码方式(备选编码方式,更加准确)

#r.content：http响应内容的二进制形式

 #####################
 # Resquests库的异常 #
 #####################

#requests.ConnectionError：网络连接错误异常,如DNS查询失败、拒绝连接等

#requests.HTTPError：HTTP错误异常

#requests.URLRequired：URL缺失异常

#requests.TooManyRedirects：超过最大重定向次数,产生重定向异常

#requests.ConnectTimeout：连接远程服务器时异常

#requests.Timeout：请求URL超时,产生超时异常

 ##########################
 # 爬取网页的通用代码框架 # 网络连接要注意异常处理
 ##########################

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
 ########################
 # HTTP协议对资源的操作 #
 ########################

#get：请求获取URL位置的资源

#head：请求获取URL位置资源的响应消息报告,即获得该资源的头部信息

#post：请求获取URL位置的资源后附加新的数据

#put：请求向URL位置存储一个资源,覆盖原URL位置的资源

#patch：请求局部更新URL位置的资源,即改变该处资源的部分内容

#delete：请求删除URL位置存储的资源

#理解put、patch的区别，以及http协议

 ##########################
 # **kwargs的13个访问参数 # 均为可选项
 ##########################

#params：字典或字节序列,作为参数增加到url中

#data：字典、字节序列或文件对象,作为Request的内容

#json：JSON格式的数据，作为request的内容

#headers：字典，HTTP定制头

#cookies：字典或CookieJar,request中的cookie

#auth：元组,支持HTTP认证功能

#files：字典类型,传输文件

#timeout：设定超时时间,秒为单位

#proxies：字典类型，设定访问代理服务器，可以增加登录认证

#allow_redirects：True/False，默认为True，重定向开关

#stream：True/False,默认为True，获取内容立即下载开关

#verify：True/False,默认为True，认证SSL证书开关

#cert：本地SSL证书路径

 ######################
 # 各类方法的参数介绍 #
 ######################

#requests.post(url,data=None,json=None,**kwargs)

##url：拟更新界面的url链接
##data,json
##**kwargs:剩余11个控制访问参数

#requests.put(url,data=None,**kwargs)

##url：拟更新界面的url链接
##data
##**kwargs:剩余12个控制访问参数

#requests.patch(url,data=None,**kwargs)

##url：拟更新界面的url链接
##data,json
##**kwargs:剩余11个控制访问参数

#requests.delete(url,**kwargs)

##url：拟删除界面的url链接
##**kwargs:剩余13个控制访问参数

#requests.get(url,params=None,**kwargs)，最常用方法

##url：拟获取界面的url链接
##params
##**kwargs:剩余12个控制访问参数









 

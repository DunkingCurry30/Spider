 ##################
 # Scrapy爬虫框架 # "5+2"结构
 ##################

#五个主要模块：
 
 #Spiders：解析downloader返回的响应（Response）
         # 产生爬取项（scraped item）
         # 产生额外的爬取请求（request）
         # 需要用户编写（配置），核心单元
         
 #Item Pipelines：以流水线形式处理Spider产生的爬取项
                # 由一组操作顺序组成，类似流水线，每个操作是一个Item Pipeline类型
                # 可能操作包括：清理、检验和查重爬取项中的HTML数据、将数据存储到数据库中
                # 需要用户编写，决定数据的去向（用途）

 #Engine：控制所有模块之间的数据流；根据条件触发事件，框架自带

 #Downloader：根据请求下载网页，不需要用户修改，框架自带

 #Scheduler：对所有的爬取请求进行调度管理，框架自带

#两个中间键：

 #Downloader Middleware:
  #目的：实施Scheduler、Downloader和Engine之间进行用户可配置的控制
  #功能：修改、丢弃、新增请求或响应
 
 #Spider Middleware：
  #目的：对请求和爬取项的再处理
  #功能：修改、丢弃、新增请求或爬取项

 ####################
 # Scrapy库常用命令 # Scrapy很多功能都是通过命令行来是实现的，在windows控制台中
 #################### 输入scrapy -h来查看命令行命令

#startproject：创建一个新工程
 #格式：scrapy startproject<name>[dir]

 #在指定文件夹创建工程后会有以下文件：

  #scrapy.cfg：部署Scrapy爬虫的配置文件（通常不需要用户配置）

  #__init__.py：初始化脚本（不需要用户配置）

  #items.py：Items代码模板(继承类),一般不需要用户编写

  #middlewares.py：Middlewares代码模板（继承类），需要用户配置

  #pipelines.py：Pipelines代码模板（继承类）

  #settings.py：Scrapy爬虫的配置文件，优化爬虫功能需要配置该项

#genspider：创建一个爬虫
 #格式：scrapy genspider[options]<name><domain>

 #执行命令后会产生一个demo.py（假定name为demo），以下为解析：

#此类继承自scrapy.Spider
class DemoSpider(scrapy.Spider):
    #名称为demo
    name = 'demo'
    #通过<domain>参数设置的域名，可以注释掉
    allowed_domains = ['python123.io']
    #初始的爬取网页的链接
    start_urls = ['http://python123.io/']

    #上述start_urls可以换为以下等价代码，且以下代码因为使用了yield关键字，对于空间资源占用十分友好：
    def start_requests(self):
        urls = ['http://python123.io/ws/demo.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    #用于处理响应，解析内容形成字典，发现新的URL爬取请求
    def parse(self, response):
        pass

#settings：获得爬虫配置信息
 #格式：scrapy settings[options]

#crawl：运行一个爬虫
 #格式：scrapy crawl<spider>

#list：列出工程中所有的爬虫
 #格式：scrapy list

#shell：启动URL调试命令行
 #格式：scrapy shell[url]

 ########################
 # Scrapy爬虫的数据类型 # 常用三个类Request，Response，Item
 ########################

#Request类：表示一个HTTP请求

 #属性：

  #.url：Request对应的请求URL地址

  #.method：对应的请求方法，'GET''POST'等

  #.headers：字典类型的请求头

  #.body：请求内容主体，字符串类型

  #.meta：用户添加的扩展信息，在Scrapy内部模块间传递信息使用

 #方法：

  #.copy()：复制该请求

#Response类：表示一个HTTP响应，由downloader生成，spider处理

 #属性：

  #.url：Response对应的URL地址

  #.status：HTTP状态吗，默认是200

  #.headers：Response对应的头部信息

  #.body：Response对应的内容信息，字符串类型

  #.flags：一组标记

  #.request：产生Response类型对应的Request对象

 #方法：

  #.copy()：复制该响应
  
#Item类：Item对象表示一个从HTML页面中提取的信息内容，由spider生成，Item Pipeline进行最终处理
       # Item类似字典类型，可以按照字典类型操作

 ########################
 # Scrapy的信息提取方式 # 主要使用CSS Selector
 ########################

#基本使用：
 <HTML>.css('a::attr(href)').extract()
 #a：标签名称
 #href：标签属性

 ####################
 # Scrapy爬虫的步骤 # 
 ####################

#步骤1：建立工程和Spider模板

#步骤2：编写Spider

#步骤3：编写ITEM Pipelines
























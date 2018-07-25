 ####################
 # Beautiful Soup库 # 解析html和xml的库
 ####################
'''
#导入
from bs4 import BeautifulSoup

#解析网页源代码demo,第二个参数是选择的解释器（这里选择html解释器html.parser)
soup = BeautifulSoup(demo,'html.parser')
'''
 ##############################
 # Beautiful Soup类的基本元素 #
 ##############################

#Tag：标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾

#Name：标签的名字，<p>...</p>的名字是'p'，格式：<tag>.name（获取标签名字）

#Attributes：标签的属性，字典形式组织，格式：<tag>.attrs

#NavigableString：标签内非属性字符串,<>...</>中字符串,格式：<tag>.string

#Comment：标签内字符串的注释部分,一种特殊的Comment类型
'''
import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
except:
    print('出现异常')

soup = BeautifulSoup(demo,'html.parser')

print(soup.a)
#获取a标签的父标签的名字
print(soup.a.parent.name)
print(soup.a.attrs)
print(soup.a.string)
'''
 ###############################
 # 基于bs4库的HTML内容遍历方法 #
 ###############################

#标签树的下行遍历：
 #.contents 属性：子节点的列表，将<tag>所有儿子节点存入列表
 #.children 属性：子节点的迭代类型，与.contents类似,用于循环遍历儿子节点
 #.descendants 属性：子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
 #（子节点不只包含标签，也包含字符串节点（例如'\n')

#标签树的上行遍历：
 #.parent 属性：节点的父亲标签
 #.parents 属性：节点先辈标签的迭代类型,用于循环遍历先辈节点

#标签树的平行遍历
 #.next_sibling 属性：返回按照HTML文本顺序的下一个平行节点标签
 #.previous_sibling 属性：返回按照HTML文本顺序的上一个平行节点标签
 #.next_siblings 属性：返回.next_sibling的迭代类型
 #.previous_sibling 属性：返回.previous_sibling的迭代类型
 #（平行遍历只能发生于同一个父亲节点下）

 ###############################
 # 基于bs4库的HTML格式化和编码 # 如何让html内容更加友好的显示
 ###############################

#prettify()方法：为html或单个标签添加换行符，借用print可以打印出来










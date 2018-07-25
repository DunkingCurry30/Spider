 ##############
 # 正则表达式 # regular expression(RE)
 ##############

#表达文本类型的特征（病毒、入侵等）

#同时查找或替换一组字符串

#匹配字符串的全部或部分

#使用时要对正则表达式字符串rex进行编译：re.compile(rex)

 ##########################
 # 正则表达式的常用操作符 # 
 ##########################

# .：表示任何的单个字符

#[]：字符集，对单个字符给出取值范围，例：[abc]表示a、b、c，[a-z]表示a到z的单个字符

#[^]：非字符集，对单个字符给出排除范围，例：[^abc]表示非a或b或c的单个字符

# *：前一个字符0次或无限次扩展，例：abc*表示ab、abc、abcc等

# + ：前一个字符1次或无限次扩展，例：abc*表示abc、abcc等

# ? ：前一个字符0次或1次扩展，例：abc?表示ab、abc

# | ：左右表达式任意一个，例：abc|def 表示abc、def

#{m}：扩展前一个字符m次，例：ab{2}c表示abbc

#{m,n}：扩展前一个字符m至n次（含n），例：ab{1,2}c表示abc,abbc

# ^ ：匹配字符串开头，例：^abc表示abc且在一个字符串的开头

# $ ：匹配字符串的结尾，例：abc$表示abc且在一个字符串的结尾

#()：分组标记，内部只能使用 | 操作符，例：(abc)表示abc,(abc|def)表示abc、def

#\d：数字，等价于{0,9}

#\w：单词字符，等价于[A-Za-z0-9_]

 ######################
 # 经典正则表达式实例 # 
 ######################

# ^[A-Za-z]+$ ：由26个英文字母组成的字符串

# ^[A-Za-z0-9]+$ ：由26个字母和数字组成的字符串

# ^-?\d+$ ：整数形式的字符串

# ^[0-9]*[1-9][0-9]*$ 正整数形式的字符串

# [1-9]\d{5} ：中国境内的邮政编码，6位

# [\u4e00-\u9fa5] ：匹配中文字符（采用UTF-8编码）

# \d{3}-\d{8}|\d{4}-\d{7} ：国内电话号码

#(([1-9]?\d|1\d{2}|2[0,4]\d|25[0,5]).){3}([1-9]?\d|1\d{2}|2[0,4]\d|25[0,5]) ：IP地址（IP地址分四段，每段0-255）

 ########
 # RE库 # 
 ########

#re库采用raw string类型表示正则表达式，表示为：r'text',raw string(原生字符串)是指不包含转义符的字符串

#主要功能函数：

 #re.search(pattern, string, flags):在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象

  #pattern：正则表达式的字符串或原生字符串表示

  #string：待匹配字符串

  #flags：正则表达式使用时的控制标记
 
   #re.I, re.IGNORECASE：忽略正则表达式的大小写，[A-Z]能匹配小写字符

   #re.M, re.MULTILINE：正则表达式中的^操作符能够将给定字符串的每行当作匹配开始

   #re.S, re.DOTALL：正则表达式中的.操作符能够匹配所有字符（默认匹配除换行外的所有字符）
import re
match = re.search(r'[1-9]\d{5}','BIT 613100')
print('search：',end="")
print(match.group(0))


 #re.match():在一个字符串的开始位置起匹配正则表达式，返回match对象,参数同search()

 #re.findall()：搜索字符串，以列表类型返回全部能匹配的字符串,参数同search()

 #re.split(pattern, string, maxsplit=0, flags=0)：将一个字符串按照正则表达式匹配结果进行分割，返回列表类型

  #maxsplit：最大分割数，剩余部分作为最后一个元素输出
split = re.split(r'[1-9]\d{5}','100081BIT 100051TSU')
print('split()：',end="")
print(split)
  
 #re.finditer()：搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素都是match对象,参数同search()

 #re.sub(pattern,repl,string,count=0,flags=0)：在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

  #repl：替换匹配字符串的字符串

  #count：匹配的最大替换次数

repl = re.sub(r'[1-9]\d{5}','zip','BIT100081 TSU100051')
print('sub()：',end="")
print(repl)

 ##################
 # Re库的两种用法 #
 ##################

#函数式：
rst = re.search(r'[1-9]\d{5}', 'BIT 100081')
#面向对象式（编译后可以进行多次操作）：
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT 100081')

 ###################
 # Re库的match对象 #
 ###################

#match对象的属性：
 # .string：待匹配的文本

 # .re：匹配时使用的pattern对象（正则表达式）

 # .pos：正则表达式搜索文本的开始位置

 # .endpos：正则表达式搜索文本的结束位置

#match对象的方法：

 # .group(0):获得匹配后的字符串

 # .start()：匹配字符串在原始字符串的开始位置

 # .end()：匹配字符串在原始字符串的结束位置

 # .span()：返回(.start(), .end())

 ############################
 # Re库的贪婪匹配与最小匹配 #
 ############################

#Re库的默认匹配模式是贪婪匹配，即总是返回匹配的最长字符串：
match = re.search(r'PY.*N','PYABNCNDN')
print('贪婪匹配：',end="")
print(match.group(0))

#最小匹配操作符

 # *? ：前一个字符0次或无限次扩展，最小匹配

 # +? ：前一个字符1次或无限次扩展，最小匹配

 # ?? ：前一个字符0次或1次扩展，最小匹配

 #{m,n}?：扩展前一个字符m至n次(含n),最小匹配
 
match = re.search(r'PY.*?N','PYABNCNDN')
print('最小匹配：',end="")
print(match.group(0))

















 ######################
 # 信息标记的三种方式 #
 ######################

#XML：通过标签形式进行信息标记，与HTML较接近

#JSON：通过有类型的键值对（键或值必须加双引号）组织信息，可以嵌套

#YAML：通过无类型的键值对,'-'表示并列关系,'|'表示整块数据,'#'进行注释

 ##################
 # 三种方式的比较 #
 ##################

#XML：可扩展性好，繁琐；用于Internet上的信息交互与传递

#实例：
 <person>
     <firstName>Stephen</firstName>
     <lastName>Sherlock</lastName>
     <address>
         <streetAddr>南岸区</streetAddr>
         <city>重庆市</city>
     </address>
     <prof>Software Engineering</prof><prof>English</prof>
 </person>
 
#JSON：信息有类型，适合程序处理，较XML简洁；用于移动应用云端和节点的信息通信，无注释

#实例：
 {
     "firstName" : "Stephen",
     "lastName"  : "Sherlock",
     "address"   : {
                        "streetAddr" : "南岸区",
                        "city"       : "重庆市"
                    }
     "prof"      : { "Software Engineering","English"}
 }
 
#YAML：信息无类型，文本信息比例最高，可读性好；各类系统的配置文件，有注释易读

#实例：
 firstName : Stephen
 lastName  : Sherlock
 address   :
     streetAddr : 南岸区
     city       : 重庆市
 prof      :
 -Software Engineering
 -English














 

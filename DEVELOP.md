#for developer

##环境搭建

##TODOS
*  选择key value数据库
*  抓取豆瓣图片的图书名，并用合适的方式储存，例如储存成纯文本文件，或者放在mysql当中等等
*  实现recall算法，生成key-value, 其中key为用户输入的内容，比如recaller的degision中提到的,`西`,`xiy`,`xi游`,`西yo`,`xyj`,`xy`,`xyouj`,`xiyj`,val为可能的suggesstion，同时把key-value用合适的方式组织起来，比如说直接通过写key-value数据库当中，或者用tries一些数据结构储存在内存当中
*  设计reranker实现方法
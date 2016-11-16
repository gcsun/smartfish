#smartfish
##who am I
这是一个搜索提示的项目，用户输入一些词之后，提示用户可能想输入的词语，提高用户的输入效率。比如：在一个电影搜索网站，在搜索框，用户已经输入“齐天”，这时候在搜索框下面，应该出现一系列可能的词，比如说“齐天大圣”，“齐天大圣前传”，供用户选择，就像google这样子的提示。
![google suggestion](img/google_suggestion.png "google suggstion")

##outline
这个项目一些计划：query suggestion，需要分成两个部分，recaller，和reranker，recaller用来召回相关的suggestion，reranker把recaller召回的suggestion进行排序。recaller需要用户提供输入的query，reranker除开用户输入的query还需要，用户提供上下文信息，这些上下文信息和rerank算法有关系。

###recaller
对于recaller初始化：程序员输入query列表，其中包含query的权重，这些权重由程序员自行离线计算得出，比如，如果是电影网站，这些query可能包括电影名称，权重应该是最新电影，热门的电影的电影名称权重更高。之后输入一个query给recaller,recaller返回通过之前程序员输入的query列表计算得出的suggestion返回给用户。

###reranker
对于reranker，因为用户的上下文不知道如何抽象，所以这一块暂时没有方案。现在github上面还没有成熟好用的项目。现在只有找到，[GitHub - syw2014/query-suggestion](https://github.com/syw2014/query-suggestion)，这个项目和query suggestion有一些关系，但是不是很成熟

##degisn

###API
* 后台考虑用**redis**一类的，key val储存, key为用户输入的内容,val为可能的suggesstion
* recaller和reranker都提供**thrift**接口，这样任何语言都可以很方便地调用

###DATA
* 考虑用豆瓣图书的所有图书名字，作为可能的suggestion候选

###algorithm

####recaller
* 汉字前缀匹配，比如，`西`，需要给出suggesstion, `西游记`，因为`西`为`西游记`的前缀，当然其它前缀也是`西`的也要给出，下面的例子也是一样，这里只举`西游记`一个例子
* 拼音前缀匹配，比如,`xiy`，需要给出suggestion,`西游记`，因为`西游记`拼音为`xiyouji`，`xiy`是`xiyouji`的前缀
* 汉字拼音前缀混合，比如`xi游`以及`西yo`，需要给出，`西游记`，
* 拼音首字母匹配，比如`xyj`或者`xy`，需要给出`西游记`
* 拼音前若干个字母匹配，比如`xyouj`或者`xiyj`，需要给出`西游记`


####rereanker

* 暂无，　等待补充


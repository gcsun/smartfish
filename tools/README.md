# Tools 使用说明

## 1. scrapy_douban_book 爬取豆瓣图书信息

### 1.1 安装scrapy库

```
pip install Scrapy
```
### 1.2 执行程序

命令行进入scrapy_douban_book文件夹，运行命令:

```
scrapy crawl books -o books_unicode.json -s CLOSESPIDER_ITEMCOUNT=1000
```
注意：
- 在文件夹下会同时生成books_unicode.json（信息以unicode编码）以及utf8_out.json（信息以utf8编码）
- CLOSESPIDER_ITEMCOUNT参数设置抓取的总数，满足条件后关闭爬虫，也可以使用参数CLOSESPIDER_TIMEOUT设置超时参数，单位是秒
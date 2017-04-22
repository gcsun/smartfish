# Tools 使用说明

## 1. scrapy_douban_book 爬取豆瓣图书信息

### 1.1 安装scrapy库

```
pip install Scrapy
```
### 1.2 执行程序

命令行进入scrapy_douban_book文件夹，运行命令:

```
scrapy crawl books -o books_unicode.json
```
注意：
- 在文件夹下会同时生成books_unicode.json（信息以unicode编码）以及utf8_out.json（信息以utf8编码）
- 由于程序会一直爬取数据，如果提前停止ctrl+C，需要打开刚才生成的两个文件，完善json数据结构
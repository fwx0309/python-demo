1. 创建爬虫的项目   scrapy startproject 项目的名字
                 注意：项目的名字不允许使用数字开头  也不能包含中文
2. 创建爬虫文件
                 要在spiders文件夹中去创建爬虫文件
                 cd 项目的名字\项目的名字\spiders
                 cd scrapy_baidu_091\scrapy_baidu_091\spiders

                 创建爬虫文件
                 scrapy genspider 爬虫文件的名字  要爬取网页
                 eg：scrapy genspider baidu  http://www.baidu.com
                 一般情况下不需要添加http协议  因为start_urls的值是根据allowed_domains
                 修改的  所以添加了http的话  那么start_urls就需要我们手动去修改了
3. 运行爬虫代码
                 scrapy crawl 爬虫的名字
                 eg：
                 scrapy crawl baidu

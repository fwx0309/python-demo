import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_crawlspider_read_33.items import ScrapyCrawlspiderRead33Item

# *** 爬取数据落到本地和 mysql 数据库中
# pip install pymysql -i https://pypi.doubanio.com/simple

# 日志设置 LOG_FILE、LOG_LEVEL(一般不做调整)
class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1179_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1179_[1-3]\.html"),
                  callback="parse_item",
                  follow=False),)

    def parse_item(self, response):
        img_list = response.xpath("//div[@class='bookslist']//img")

        for img_obj in img_list:
            # get() 和 extract_first() 效果一样
            name = img_obj.xpath("./@alt").get()
            img = img_obj.xpath("./@data-original").get()
            # print("%s - %s" % (name, img))

            yield ScrapyCrawlspiderRead33Item(name=name, img=img)
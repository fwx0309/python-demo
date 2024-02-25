import scrapy
from scrapy_dangdang_31.items import ScrapyDangdang31Item


# 使用 items 和 pipelines 步骤
# 1.items 中定义数据字段，dangdang.py 中用 yield 返回 items对象（ScrapyDangdang31Item，需要 import 类）
# 2.settings.py 中打开 ITEM_PIPELINES 设置
# 3.pipelines.py 中写出数据。
# 4.多条管道，可以模仿 pipelines.py 中原有的类写，注意在 settings.py 添加新写的管道

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    # 如果要下载多页数据，只保留允许访问的域名：category.dangdang.com
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    # 除第一页的 base url
    base_url = "http://category.dangdang.com/pg"
    page = 1;

    def parse(self, response):
        print("===========================")
        li_list = response.xpath("//ul[@id='component_59']/li")

        for li in li_list:
            img = li.xpath(".//img/@data-original").extract_first()
            if img:
                img = img
            else:
                img = li.xpath(".//img/@src").extract_first()

            name = li.xpath(".//img/@alt").extract_first()
            price = li.xpath("./p[@class='price']/span[1]/text()").extract_first()
            print("%s, %s, %s" % (name, price, img))
            print("---")

            # 返回数据到管道中
            yield ScrapyDangdang31Item(img=img, name=name, price=price)

        # 多页数据下载，需要再次调用 parse 方法，下载后面页数据
        # 第一页：http://category.dangdang.com/cp01.01.02.00.00.00.html
        # 第二页：http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        # 第三页：http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        # 第一页已经执行，执行后面页数即可
        # 剩余页数据下载，由于数据太多，这里只下载3页
        if self.page < 3:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + "-cp01.01.02.00.00.00.html"
            # 注意：parse 不要加括号
            yield scrapy.Request(url=url, callback=self.parse)

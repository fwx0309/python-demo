import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["wh.58.com"]
    start_urls = ["https://wh.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]

    def parse(self, response):
        print("--------------------------")
        # print(response.text)
        # print(response.body)
        span = response.xpath("//div[@id='filter']/div[@class='tabs']//span")[0]
        print(span.extract())
        print("--------------------------")


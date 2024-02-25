import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]

    # scrapy 中 post 请求，不使用 start_urls 和 parse()
    # start_urls = ["https://fanyi.baidu.com/sug"]
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "https://fanyi.baidu.com/sug"

        data = {
            'kw': 'fina'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        json_obj = json.loads(content)

        print(json_obj)

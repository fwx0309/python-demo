import scrapy
from scrapy_moviesky_32.items import ScrapyMoviesky32Item

class MovieskySpider(scrapy.Spider):
    name = "moviesky"
    allowed_domains = ["dygod.net"]
    start_urls = ["https://dygod.net/html/gndy/china/index.html"]

    def parse(self, response):
        print("============== 1 ===============")
        a_list = response.xpath("//div[@class='co_content8']//a[2]")

        for a in a_list:
            title = a.xpath("./text()").extract_first()
            img_url = a.xpath("./@href").extract_first()
            img_url = "https://dygod.net" + img_url
            print("%s - %s" % (title, img_url))

            # 二次访问。将第一次请求页面中的图片 url 当做请求地址，并将 title 传入第二次请求中。
            yield scrapy.Request(url=img_url,callback=self.parse2,meta={"title":title})

    # 自定义第二次请求方法
    def parse2(self, response):
        print("============== 2 ===============")
        img = response.xpath("//div[@id='Zoom']/img[1]/@src").extract_first()
        img = "https://dygod.net" + img

        yield ScrapyMoviesky32Item(title=response.meta["title"],img=img)
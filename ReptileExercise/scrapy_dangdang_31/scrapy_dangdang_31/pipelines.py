# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdang31Pipeline:
    # 爬虫执行前执行
    def open_spider(self, spider):
        # 这里的相对路径，是相对于 dangdang.py 的路径
        self.fp = open("../data/dangdang_json_data.json","a",encoding="utf-8")
        print("****** open file: data.json ******")

    def process_item(self, item, spider):
        self.fp.write(str(item)+",")
        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        self.fp.close()
        print("****** close file: data.json ******")

# 自定义下载管道
import urllib.request
import time
class ScrapyDangdang31ImgDownloadPipeline:
    def process_item(self, item, spider):
        img_url = item['img']
        name = item.get("name")
        urllib.request.urlretrieve("http:"+img_url,"../img/"+name+".jpg")
        # 书名中有特殊符号时会报错
        # urllib.request.urlretrieve("http:"+img_url,"../img/"+str(time.time())+".jpg")
        return item
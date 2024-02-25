# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyCrawlspiderRead33Pipeline:
    def open_spider(self, spider):
        self.fp = open("../data/readbook.json","w",encoding="utf-8")

    def process_item(self, item, spider):
        self.fp.write(str(item)+",")
        return item

    def close_spider(self, spider):
        self.fp.close()

# 把数据存到 mysql 的管道
from scrapy.utils.project import get_project_settings
import pymysql
class MysqlPipeline:
    # 这里是调用 open_spider 方法来初始化 mysql，也可以替换为 def __init__(self):
    def open_spider(self, spider):
        settings = get_project_settings()
        self.mysql_host = settings['MYSQL_HOST']
        self.mysql_port = settings['MYSQL_PORT']
        self.mysql_user = settings['MYSQL_USER']
        self.mysql_password = settings['MYSQL_PASSWORD']
        self.mysql_db = settings['MYSQL_DB']
        self.mysql_charset = settings['MYSQL_CHARSET']

        print("*********** mysql 参数 ************")
        print(self.mysql_host)
        print(self.mysql_port)
        print(self.mysql_user)
        print(self.mysql_password)
        print(self.mysql_db)
        print(self.mysql_charset)
        print("***********************************")

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.mysql_host,
                                    port=self.mysql_port,
                                    user=self.mysql_user,
                                    password=self.mysql_password,
                                    db=self.mysql_db,
                                    charset=self.mysql_charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name,img) values("{}","{}")'.format(item['name'],item['img'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
        # pass
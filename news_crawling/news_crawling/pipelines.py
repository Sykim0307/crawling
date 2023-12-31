# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from settings import MONGODB_URI, MONGODB_PORT
from pymongo import MongoClient
class NewsCrawlingPipeline:
    def open_spider(self, spider):
        print("Open Spider : ", spider)
        self.db = MongoClient(MONGODB_URI, MONGODB_PORT)    
    def close_spider(self , spider):
        print("Close Spider : ", spider)
    
    def exporter_
    
    def process_item(self, item, spider):
        
        return item

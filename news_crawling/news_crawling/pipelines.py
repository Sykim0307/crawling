# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem
import json
import logging

class JSONWriterPipeline:
    
    def open_spider(self, spider):
        self.file = open('yna_news.json','w')
        self.file.write('{')
    def close_spider(self,spider):
        self.file.write('}')
        self.file.close()
    def process_item(self, item, spider):
        try:
            item_dict = ItemAdapter(item).asdict()
            item_dict['date'] = str(item_dict['date'])
            
            line = json.dumps(item_dict) + ',\n'
            self.file.write(line)
        except :
            breakpoint()
        return item
    
class NewsCrawlingPipeline:
    collection_name = 'article'
    
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri 
        self.mongo_db =mongo_db
    @classmethod
    def from_crawler(cls, crawler):
        
        return cls(
            mongo_uri = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DATABASE")
        )
    def open_spider(self, spider):
        self.client= MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        print("==>Open Spider : ", spider, "Client : ", self.client ,"DB : ", self.db)
        
    def close_spider(self , spider):
        
        print("==>Close Spider : ", spider)
        self.client.close()
        
    def process_item(self, item, spider):
        print("==>Process Item : " , "spider : ",  spider, " item : ", item)
        
        try:
            print("== Validation Start ==")
            item.validate()
            
            print("== Normalization Start ==")
            item.normalize()
            
            print("DB INSERT ONE")
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        except :
            breakpoint()    
        return item
        
        
        

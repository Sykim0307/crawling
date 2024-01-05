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
        spider.log(f"==>Open Spider : {spider.name} | Clinet : {self.client}  | DB : {self.db}")
        
    def close_spider(self , spider):
        
        spider.log(f"==>Close Spider : {spider.name}", )
        self.client.close()
        
    def process_item(self, item, spider):
        spider.log(f"==>Process Item ::: spider : {spider.name}  | item : {item} ")
        
        try:
            # validate
            spider.log('== Validation Start ==')
            #print("== Validation Start ==")
            item.validate()
            
            # normalize
            spider.log("== Normalization Start ==")
            #print("== Normalization Start ==")
            item.normalize()
            
            # 중복제거
            
            exist_doc = self.db[self.collection_name].find_one({'url':item.url})
            if exist_doc :
                spider.log("== DB UPDATE ONE ==")
                self.db[self.collection_name].update_one(
                    {'url':item.url},
                    {'$set':ItemAdapter(item).asdict()} # 더 최신의 것으로 update
                )
                
            else:
                # insert
                spider.log("== DB INSERT ONE == ")
                self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
                
        except :
            breakpoint()    
        
        
        
        return item
        
        
        

""" 
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
     """
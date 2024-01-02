# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
import scrapy
from scrapy import Field

@dataclass
class NewsCrawlingItem:
    
    url : str = field(default=None)# 뉴스 링크
    title : str = field(default=None) # 뉴스 제목
    date : datetime = field(default=None)# 작성일
    writer: str = field(default=None)# 뉴스 작성한 기자
    content: str = field(default=None) # 뉴스 기사
    name : str = field(default=None) # 뉴스 회사 ( ex) 연합뉴스 )
    img : str = field(default=None) # 기사 thumbnail 이미지
    
    def normalize(self):    
        return
    
    def validate(self):
        self.str_validate(self.url)
        self.str_validate(self.title)
        self.str_validate(self.writer)
        self.str_validate(self.content)
        self.str_validate(self.name)
        self.str_validate(self.img)
        self.datetime_validate(self.date)
        
        
    @staticmethod
    def str_validate(str_data):
        if str_data != None and not isinstance(str_data, str):
            raise TypeError(f"{str_data} is Wrong")
    @staticmethod
    def datetime_validate(datetime_data):
        if datetime_data != None and not isinstance(datetime_data, datetime):
            raise TypeError(f"{datetime_data} is Wrong")
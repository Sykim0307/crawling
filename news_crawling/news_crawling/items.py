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
class Time :
    # 대한민국은 UTC+09:00 ( 동경 135도 기준 시간대를 이용한다. ) 로 UTC(런던)보다 9시간 빠르다. 
    year : int = field(default = None)
    month : int = field(default = None)
    day : int = field(default = None)
    hour : int = field(default = None)
    minute : int = field(default = None)
    timezone : str = field(default =None) # UTC 시간대
    
    def validate(self):
        if self.year!=None and (self.year>2025 or self.year < 2000) :
            raise TypeError(f"year is Wrong : {self.year}")
        
        if self.month!= None and (self.month < 1 or self.month>12):
            raise TypeError(f"month is Wrong : {self.month}")
        
        if self.day!=None and (self.day < 1 or self.day > 31) :
            raise TypeError(f"day is Wrong : {self.day}")

        if self.hour!=None and (self.hour < 0 or self.hour>24):
            raise TypeError(f"hour is Wrong : {self.hour}")
        
        if self.minute!=None and (self.minute < 0 or self.minute > 60):
            raise TypeError(f"minute is Wrong : {self.minute}")
        
        
        
@dataclass
class NewsCrawlingItem:
    
    url : str = field(default=None)# 뉴스 링크 - crawl id 로 사용
    title : str = field(default=None) # 뉴스 제목
    updated_date : Time = field(default_factory=Time) # 뉴스가 업데이트된 날짜
    published_date : Time = field(default_factory= Time) # 뉴스가 출판된 날짜
    read_time : int = field(default=None) # 뉴스 읽는데 걸리는 "단위 분"
    writer: str = field(default=None)# 뉴스 작성한 기자
    content: str = field(default=None) # 뉴스 기사
    name : str = field(default=None) # 뉴스 회사 ( ex) 연합뉴스 )
    img : str = field(default=None) # 기사 thumbnail 이미지
    crawled_time : datetime = field(default=datetime.now())
    
    #deprecated
    #date : datetime = field(default=None)# 작성일
    
    
    def normalize(self):    
        return
    
    def validate(self):
        self.str_validate(self.url)
        self.str_validate(self.title)
        self.str_validate(self.writer)
        self.str_validate(self.content)
        self.str_validate(self.name)
        self.str_validate(self.img)
        self.int_validate(self.read_time)
        self.updated_date.validate()
        self.published_date.validate()
        
        #deprecated
        #self.datetime_validate(self.date)
        
        
    
    @staticmethod
    def int_validate(int_data):
        if int_data != None and not isinstance(int_data, int):
            raise TypeError(f"{int_data} is Wrong")

    @staticmethod
    def str_validate(str_data):
            if str_data != None and not isinstance(str_data, str):
                raise TypeError(f"{str_data} is Wrong")
            
    @staticmethod
    def datetime_validate(datetime_data):
            if datetime_data != None and not isinstance(datetime_data, datetime):
                raise TypeError(f"{datetime_data} is Wrong")
        
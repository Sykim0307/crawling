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
    
    url : str 
    title : str
    img : str = field(default=None)
    date : datetime
    writer: str
    content: str
    
    def normalize(self):
        
    def validation(self):
        
    

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup 
import logging
from items import NewsCrawlingItem

class NewsSpider(scrapy.Spider):
    name ='news'
    custom_settings={
        'LOG_FILE' : 'yna_news.log',
        
    }
    allowed_domains = ['www.yna.co.kr']
    
    sitemap_url ='https://www.yna.co.kr/sitemap.xml'
    list_page_ex ='https://www.yna.co.kr/news?site=navi_latest_depth01'
    def start_requests(self):
        print('1')
        
        yield Request(
            url = self.sitemap_url,
            callback = self.parse
        )    
    def parse(self,response):
        logging.info(f'parse => response url : {response.url}')
        soup = BeautifulSoup(response.text ,'xml')
        links = soup.select('loc')
        
        for link in links :
            if 'https://www.yna.co.kr/news-sitemap3.xml' in link.text:
                yield Request(
                    url=link.text,
                    callback=self.parse_sitemap
                )
        
        print(soup)
    def parse_sitemap(self,response):
        logging.info(f'parse_sitemap => response url : {response.url}')
        soup = BeautifulSoup(response.text , 'xml')
        links = soup.select('loc')
        for link in links:
            yield Request(
                url=link.text,
                callback = self.parse_news
            )
            
        logging.info(f"Total News Count : {len(links)}")
    
    def parse_news(self,response):
        logging.info(f'parse_news ==> response url : {response.url}')
        soup = BeautifulSoup(response.text , 'html.parser')
        
        # make dict and record url
        news_info = {}
        news_info['url'] = response.url
        news_info['title'] = soup.find('h1', class_='tit').text
        news_info['date']=soup.find('p', id='newsUpdateTime01').get('data-published-time')
            
        # parse article information
        try:
            news_info['writer'] = soup.find('strong', class_='tit-name').text
        except Exception as e:
            print("==> Error in Parse writer : ", e) 
            
        try:
            news_info['img'] = 'https:'+soup.find('span', class_='img').find('img').get('src')
        except Exception as e:
            print("==> Error in Parse img : ", e) 
            
        try:
            articles = soup.find('div', class_='content01 scroll-article-zone01').find_all('p')
            news_info['article'] = ' '.join([article.text.strip() for article in articles])
        except Exception as e:
            print("==> Error in Parse Article : ", e) 
        
        # check result
        print("=========================================")
        for key, val in news_info.items():
            print(f'[{key}] : {val}')
        print("=========================================")
            
        
        NewsCrawlingItem(
            
        )
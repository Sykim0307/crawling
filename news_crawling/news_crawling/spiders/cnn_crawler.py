import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup 
import logging
from datetime import datetime
from ..items import ( NewsCrawlingItem , Time )
import re

class NewsSpider(scrapy.Spider):
    
    # CNN 사이트에서 전 분야 뉴스 크롤링
    name ='cnn_news'
    custom_settings={
        'LOG_FILE' : 'cnn_news.log',
    }
    allowed_domains = ['edition.cnn.com']
    
    sample_news = 'https://edition.cnn.com/2024/01/03/tech/oklahoma-teenager-defeats-tetris/index.html'
    cnn_url ='https://edition.cnn.com/'
    
    def start_requests(self) :
        yield Request(
            url=self.cnn_url,
            callback=self.parse_list_page
        )
    
    # parse list page
    def parse_list_page(self,response):
        logging.info(f'parse_list_page ==> response.url : {response.url}')
        soup = BeautifulSoup(response.text , 'html.parser')
        
        lis = soup.find('nav', class_='subnav').find_all('a')
        links = [ li.get('href') for li in lis ]
        
        # 각각의 뉴스 리스트 페이지로 Request
        for link in links :
            yield Request(
                url=link,
                callback=self.parse_news_list,
            )
        
    # news list page -> detail page parsing
    def parse_news_list(self,response):
        logging.info(f'parse_news_list ==> response url : {response.url}')
        soup = BeautifulSoup(response.text, 'html.parser')
        a_links = soup.find_all('a')
        
        news_list = []
        
        for link in a_links :
                url = link.get('href')
                
                if url != None:
                    if url.endswith('.html') :
                        if not url.startswith('https'):
                            url = 'https://edition.cnn.com' +url
                            news_list.append(url)
    
        # 중복 제거                
        news_list = list(set(news_list))
        print(f"{response.url} ==> Total News Count : " , len(news_list))
        
        for news in news_list :
            yield Request(
                url = news,
                callback = self.parse_news
            )
    
    # news 상세 페이지 parsing
    def parse_news(self,response):
        logging.info(f"parse_news ==> response url :{response.url}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_info = {}
        
        # 제목 수집
        try:
            news_info['title'] = soup.find('div', class_='headline__wrapper').find('h1').text.strip()
        except :
            pass
        # 이미지 - 수집 x
        
        # 작성일 수집
        try:
            date_info = soup.find('div', class_='headline__byline-sub-text').text.lower().strip()
            
            # read time
            search_read_time = re.search(r'\d minute read',date_info)
            if search_read_time :
                
                news_info['read_time'] = int(search_read_time.group(0).replace('minute read',''))
                date_info = date_info.replace(search_read_time.group(0),'').strip()
            
            # update time
            if 'updated' in date_info:
                
                date_info = date_info.replace('updated','').replace('\n','').strip()
                rt_val = self.parse_date_info(date_info)
                if rt_val != -1 :
                    news_info['updated_time'] = Time(
                        year=rt_val.get('year'),
                        month=rt_val.get('month'),
                        day=rt_val.get('day'),
                        hour=rt_val.get('hour'),
                        minute=rt_val.get('minute'),
                        timezone=rt_val.get('timezone')
                    )
                else :
                    print("Input Data : " , date_info , " -> You Need to Check This URL For Updated Time Check ==> ", response.url)
                    
                    
            elif 'published' in date_info:
                
                date_info = date_info.replace('published','').replace('\n','').strip()
                rt_val = self.parse_date_info(date_info)
                if rt_val != -1 :
                    news_info['published_time'] = Time(
                        year=rt_val.get('year'),
                        month=rt_val.get('month'),
                        day=rt_val.get('day'),
                        hour=rt_val.get('hour'),
                        minute=rt_val.get('minute'),
                        timezone=rt_val.get('timezone')
                    )
                else :
                    print("Input Data : " , date_info , " -> You Need to Check This URL For Published Time Check ==> ", response.url)
                    
            
        except :
            pass
        
        # 내용 
        try:
            content_div = soup.find('div', class_='article__content')
            erase_gap_in_content_div = re.sub(r'\s+',' ',content_div.text)
            #print(erase_gap_in_content_div)
            news_info['article'] = erase_gap_in_content_div
        except :
            pass 
          
        #기자 
        try:
            news_info['writer'] = soup.find('span', class_='byline__name').text
        except:
            pass
        
        
        # news item 생성 및 yield 
        try:
            news = NewsCrawlingItem(
                name='cnn',
                url = response.url,
                title=news_info.get('title'),
                published_date= news_info.get('published_time',Time()),
                updated_date= news_info.get('updated_time',Time()),
                read_time=news_info.get('read_time'),
                writer=news_info.get('writer'),
                content=news_info.get('article')
            )
        
            yield  news 
            
        except:
            breakpoint()   
    
    @staticmethod
    def parse_date_info(date_info : str) :
        # [ 2:18 pm edt, wed april 12, 2023 ] format 의 string 데이터 파싱
        infos = date_info.split(',')
        time_info={} 
        if len(infos) != 3 :
            return -1
        # year
        if len(infos[-1].strip()) == 4:
            time_info['year'] = int(infos[-1].strip())
        
        # month , day
        month_and_day = infos[1].strip().split()
        if len(month_and_day) != 3 :
            return -1
        time_info['day'] = int(month_and_day[-1])
        
        month_str = month_and_day[1]
        if month_str == 'january':
            time_info['month'] = 1
        elif month_str == 'feburary':
            time_info['month'] = 2
        elif month_str == 'march':
            time_info['month'] = 3
        elif month_str == 'april':
            time_info['month'] = 4
        elif month_str == 'may':
            time_info['month'] = 5
        elif month_str == 'june':
            time_info['month'] = 6
        elif month_str == 'july':
            time_info['month'] = 7
        elif month_str == 'august':
            time_info['month'] = 8
        elif month_str == 'september':
            time_info['month'] = 9
        elif month_str == 'october':
            time_info['month'] = 10
        elif month_str == 'november':
            time_info['month'] = 11
        elif month_str == 'december':
            time_info['month'] = 12
            
        
        # hour, minute 
        hour_and_minute = infos[0].strip().split()
        if len(hour_and_minute) != 3 :
            return -1
        
            
        
        if hour_and_minute[1] == 'am':
            time_info['hour']=int(hour_and_minute[0].split(':')[0]) 
            time_info['minute']=int(hour_and_minute[0].split(':')[1])
        elif hour_and_minute[1] == 'pm':
            time_info['hour']=int(hour_and_minute[0].split(':')[0])  + 12
            time_info['minute']=int(hour_and_minute[0].split(':')[1]) 
        time_info['timezone'] =  hour_and_minute[2]
        
        return time_info 
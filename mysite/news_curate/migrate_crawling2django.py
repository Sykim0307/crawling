from pymongo import MongoClient
from datetime import datetime
from .models import Article
"""
    Be Careful !! It's migrate code ( crawling data to service DB )
"""
def migration():
    mongo_uri = 'mongodb://localhost:27017'
    mongo_db = 'news_db'
    client = MongoClient(mongo_uri)
    db = client[mongo_db]

    django_news_collection = db['django_news']
    article_collection = db['article']

    # crawling project collection
    crawling_docs = article_collection.find({},{'_id':0,'name':0,'img':0,'crawled_time':0})
    crawling_data_list = [doc for doc in crawling_docs]
    print("Total Crawling Data Count : ", len(crawling_data_list))

    # django project collection
    django_docs = django_news_collection.find({},{'_id':0})
    django_data_list = [doc for doc in django_docs]
    print("Total Django Data Count : ", len(django_data_list))

    for data in crawling_data_list :
        # check duplicated data 
        
        # slug 생성
        try:
            article_url = data['url']
            article_url = article_url.replace('https://edition.cnn.com/','').replace('/index.html','')
            data['slug'] = '-'.join(article_url.split('/'))
        except Exception as e:
            print("Error in Making News Slug ==> Error Message : ", e)
            print("Original Data ( URL ) : ", article_url)
        # updated time (dict) 을 datetime으로 변경
        try:
            u_time_dict = data['updated_date']
            p_time_dict = data['published_date']
                
            if u_time_dict['year'] != None :
                if u_time_dict['hour'] == 24 :
                    u_time_dict['hour'] = 0
                data['updated_date']=datetime(u_time_dict['year'],u_time_dict['month'],u_time_dict['day'],u_time_dict['hour'],u_time_dict['minute'])
                data['published_date'] = None
            elif  p_time_dict['year'] != None:
                
                if p_time_dict['hour'] == 24 :
                    p_time_dict['hour'] = 0
                
                data['published_date']=datetime(p_time_dict['year'],p_time_dict['month'],p_time_dict['day'],p_time_dict['hour'],p_time_dict['minute'])
                data['updated_date'] = None
        except Exception as e:
            continue # 날짜가 비정상적이면 일단 pass
            
        duplicate_doc = django_news_collection.find_one({'url':data['url']}) 
        
        # 기존에 있는 문서라면  더 최신의 것으로 update
        if duplicate_doc :    
            django_news_collection.delete_one({'url':data['url']})
            # Make Article Object
            article = Article(
                url = data['url'],
                slug = data['slug'],
                title = data['title'],
                content = data['content'],
                read_time = data['read_time'],
                writer = data['writer'],
                update_date = data['updated_date'],
                published_date = data['published_date'] 
            )
            article.save()
            
            #django_news_collection.insert_one(data)
            #print(f"Update ==> url : {data['url']}")
            
        else:
            django_news_collection.insert_one(data)
            #print(f"Insert ==> url : {data['url']}")
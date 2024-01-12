#from django.db import models
from djongo import models

# 뉴스 데이터
class Article(models.Model):
    url = models.CharField(max_length = 50)
    slug = models.CharField(max_length=50)
    title = models.CharField(max_length = 50)    
    content = models.CharField(max_length = 400)    
    read_time = models.IntegerField()
    writer = models.CharField(max_length = 50)
    updated_date =  models.DateTimeField('updated date')
    published_date = models.DateTimeField('published date')
    
    class Meta: # 
        db_table  = 'django_news' # DB에 자동으로 django_news 라는 collection에 적재된다.


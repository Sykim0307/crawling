#from django.db import models
from djongo import models

# Create your models here.
""" class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) """

# 뉴스 데이터
class Article(models.Model):
    url = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)    
    content = models.CharField(max_length = 400)    
    pub_date = models.DateTimeField("date published") # 데이터 생성일
    
    class Meta: # 
        abstract = True
        db_table = 'django_news' # DB에 자동으로 django_news 라는 collection에 적재된다.

class Entry(models.Model):
    news = models.EmbeddedField(
        model_container = Article
    )
    headline = models.CharField(max_length = 255)


""" 
# 사용자가 본 뉴스 기록
class ArticleChoice(models.Model):
    url = models.ForeignKey(Article , on_delete = models.CASCADE)
    username = models.CharField(max_length = 50)
    pub_date = models.DateTimeField("date published") # 데이터 생성일 """
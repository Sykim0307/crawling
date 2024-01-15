#from django.db import models
from djongo import models
from django.forms import ModelForm
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location='/media/photos')

# 뉴스 데이터
class Article(models.Model):
    url = models.URLField(max_length = 50)
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length = 50)    
    content = models.CharField(max_length = 400)    
    read_time = models.PositiveSmallIntegerField()
    writer = models.CharField(max_length = 50)
    updated_date =  models.DateTimeField('updated date')
    published_date = models.DateTimeField('published date')
    
    class Meta: # 
        db_table  = 'django_news' # DB에 자동으로 django_news 라는 collection에 적재된다.

class UserModel(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    nickname = models.CharField(max_length=30, unique=True)
    pwd = models.CharField(max_length=30)
    email = models.EmailField()
    #profile = models.ImageField(upload_to='uploads')
    
    def __userInfo__(self):
        print("== User Info ==")
        print(f'[ ID ] : {self.id}')
        print(f'[ NAME ] : {self.nickname}')
        print(f'[ EMAIL ] : {self.email}')
        print("===============")
    
    class Meta:
        db_table='django_users'  

    # 저작권 표시   
    # <a href="https://www.flaticon.com/kr/free-icons/" title="프로필 아이콘">프로필 아이콘  제작자: SBTS2018 - Flaticon</a>
        
class UserForm(ModelForm): # 회원가입시 이용
    class Meta:
        model=UserModel
        fields='__all__'



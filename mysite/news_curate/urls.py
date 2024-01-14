from django.urls import path
from news_curate.views import (ArticleListView , ArticleDetailView
                               , UserCreateView
                               ,LoginView
                               )

app_name = 'news_curate'
urlpatterns = [
    path("", ArticleListView.as_view() , name='article-list'), # 뉴스 리스트 페이지
    path("news/<slug:slug>/",ArticleDetailView.as_view(), name='detail_test'), # 뉴스 상세 페이지
    path("signup/",UserCreateView.as_view(), name='signup'), # 회원가입
    path("signin/",LoginView.as_view(), name='signin'), # 로그인
    
    
    
]
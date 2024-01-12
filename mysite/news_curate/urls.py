from django.urls import path
from news_curate.views import ArticleListView , ArticleDetailView, ArticleDetailUsingDetailView

app_name = 'news_curate'
urlpatterns = [
    path("", ArticleListView.as_view() , name='article-list'),
    #path("<slug:id>/", ArticleDetailView.as_view(), name='article-detail')
    path("<str:news_slug>/",ArticleDetailView, name='detail'),
    path("test/<slug:news_slug>/",ArticleDetailUsingDetailView.views(), name='detail_test')
    
]
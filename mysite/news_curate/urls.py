from django.urls import path
from news_curate.views import ArticleListView 

app_name = 'news_curate'
urlpatterns = [
    path("", ArticleListView.as_view() ),
    #path("<int:question_id>/", views.DetailView.as_view(), name="detail"),
    #path("<int:question_id>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]
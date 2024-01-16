from django.urls import path
from news_curate.views import (ArticleListView , ArticleDetailView
                               ,LoginView, SignUpView, logout_view
                               ,mypage, LoginView_AUTH,LogOutView_AUTH
                               )



app_name = 'news_curate'
urlpatterns = [
    #content
    path("", ArticleListView.as_view() , name='article-list'), # 뉴스 리스트 페이지
    path("news/<slug:slug>/",ArticleDetailView.as_view(), name='detail_test'), # 뉴스 상세 페이지
    
    #user
    path("accounts/login", LoginView_AUTH.as_view(), name='login'),
    path('accounts/logout',LogOutView_AUTH.as_view(), name='logout'),
    path("accounts/signup",SignUpView.as_view(), name='signup'), # 회원가입
    path('accounts/mypage', mypage, name='mypage'),
    
    #deprecated
    #path('logout/',logout_view, name='logout'),
    #path("signin/",LoginView.as_view(), name='signin'), # 로그인
    #path("test-login", auth_views.LoginView.as_view(template_name = 'news_curate/test-login.html'),name='test-login'),
    #path('change-passwd/', auth_views.PasswordChangeView.as_view(template_name = 'news_curate/test-changepwd.html'), name='changepwd'),
]
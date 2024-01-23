from django.urls import path
from news_curate.views import (ArticleListView , ArticleDetailView
                               , SignUpView,mypage, LoginView_AUTH,
                               LogOutView_AUTH,ChangePWD_AUTH,ChangePWDDone_AUTH,
                               ResetPassword_AUTH,ResetPasswordDone_AUTH,ResetPasswordConfirm_AUTH
                               )



app_name = 'news_curate'
urlpatterns = [
    #content
    path("", ArticleListView.as_view() , name='article-list'), # 뉴스 리스트 페이지
    path("news/<slug:slug>/",ArticleDetailView.as_view(), name='detail_test'), # 뉴스 상세 페이지
    
    #user
    path("accounts/login", LoginView_AUTH.as_view(), name='login'), # 로그인
    path('accounts/logout',LogOutView_AUTH.as_view(), name='logout'), #로그아웃
    path("accounts/signup",SignUpView.as_view(), name='signup'), # 회원가입
    path('accounts/mypage', mypage, name='mypage'), # 마이페이지
    path('accounts/changepwd', ChangePWD_AUTH.as_view()  , name='password_change'), #패스워드변경
    path('accounts/changepwddone' , ChangePWDDone_AUTH.as_view()), # 패스워드변경확인
    path('accounts/resetpwd' , ResetPassword_AUTH.as_view() , name = 'password_reset'), # 패스워드 재설정
    path('accounts/resetpwddone', ResetPasswordDone_AUTH.as_view(), ), #패스워드재설정완료
    path('accounts/resetpwdconfirm', ResetPasswordConfirm_AUTH.as_view(), name='password_reset_confirm' ) #패스워드 재설정 확인
    #deprecated
    #path('logout/',logout_view, name='logout'),
    #path("signin/",LoginView.as_view(), name='signin'), # 로그인
    #path("test-login", auth_views.LoginView.as_view(template_name = 'news_curate/test-login.html'),name='test-login'),
    #path('change-passwd/', auth_views.PasswordChangeView.as_view(template_name = 'news_curate/test-changepwd.html'), name='changepwd'),
]
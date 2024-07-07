from django.views.generic import ListView, DetailView
from .models import  Article, UserForm , UserModel
from .custom_forms import NameForm, LoginForm , SignUpForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth import views as auth_views

# Article List Page
class ArticleListView(ListView): 
    model = Article
    queryset=Article.objects.order_by('-published_date').exclude(published_date = None )
    paginate_by = 100
    template_name = 'news_curate/article-list.html'

# Article Detail Page
class ArticleDetailView(DetailView): 
    model= Article
    template_name ='news_curate/artilce-detail.html' 
    context_object_name = 'article'
    
# Sign up
class SignUpView(FormView):
    template_name='news_curate/signup.html'
    form_class = SignUpForm
    success_url = '/news_curate/'
    
    def form_valid(self, form):
        print("SignUpView : Form is Valid ! ")
        val = form.make_user()
        if val == -1 :
            self.success_url = '/news_curate/accounts/signup'
        else :
            print(f"Sing Up Success ! \n - Welcome {val}")
        return super().form_valid(form)
    
# Login
class LoginView_AUTH(auth_views.LoginView):
    template_name = 'news_curate/account-login.html'
    next_page = '/news_curate/'
    
# Logout
class LogOutView_AUTH(auth_views.LogoutView):
    template_name = 'news_curate/account-logout.html'
    next_page = '/news_curate/'
    
# Change Password
class ChangePWD_AUTH(auth_views.PasswordChangeView):
    template_name = 'news_curate/account-changepwd.html'
    success_url = '/news_curate/accounts/changepwddone'
class ChangePWDDone_AUTH(auth_views.PasswordChangeDoneView):
    template_name = 'news_curate/account-changepwddone.html'

# Reset Passwrod
class ResetPassword_AUTH(auth_views.PasswordResetView):
    template_name ='news_curate/account-resetpwd.html'
    email_template_name = 'news_curate/account-resetpwd-email.html'
    success_url = '/news_curate/accounts/resetpwddone'
class ResetPasswordDone_AUTH(auth_views.PasswordResetDoneView):
    template_name = 'news_curate/account-resetpwddone.html'
class ResetPasswordConfirm_AUTH(auth_views.PasswordResetConfirmView):
    template_name='news_curate/account-resetpwdconfirm.html'
class ResetPasswordComplete_AUTH(auth_views.PasswordResetCompleteView):
    template_name='news_curate/account-resetpwdcomplete.html'
    
# My page
@login_required(login_url='/news_curate/accounts/login')
def mypage(request):
    if request.user.is_authenticated:
        print("AUTH USER : ", request.user.username)
        return render(request, 'news_curate/account-mypage.html', {'user' : request.user})    
    else:
        print("ERROR ?? ")


# depreacted
"""     
   
#로그아웃
def logout_view(request):
    try:
        print("== logout_view ==")
        if request.user.is_authenticated :
            print("AUTH USER : ", request.user)
        else:
            print("NOT AUTH ")
        print("===============")
        
        logout(request)  
        

    except Exception as e :
        print("LOG OUT ERROR ? : ", e)
    return HttpResponseRedirect('/news_curate/')  
#로그인 뷰
class LoginView(FormView):
    template_name = 'news_curate/signin.html'
    form_class = LoginForm
    success_url = '/news_curate/'
    
    def form_valid(self, form):
        print("LoginView : Form is Valid !  : ", self.request)
        val = form.validate(self.request)
        if val == -1 :
            self.success_url = '/news_curate/signin'
        else:
            print(f"Log in Success ! \n - Welcome {val.username}")
            #login(request,val)
        return super().form_valid(form)

#로그인 뷰
class LoginView(FormView):
    template_name = 'news_curate/signin.html'
    form_class = LoginForm
    success_url = '/news_curate/'

    def form_valid(self, form):
        print("LOGIN : Form is Valid ! ")
        val = form.validate()
        if val == False :
            self.success_url =  '/news_curate/signin'       
        return super().form_valid(form)
            """
""" #회원가입 뷰
class UserCreateView(CreateView):
    model = User
    fields='__all__'
    success_url='/news_curate/'
    template_name='news_curate/signup.html'
 """
""" 
# 회원가입
def signup_view(request): 
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("SIGN UP SUCCESS ==> ID :  ", request.POST['id'] )
            return HttpResponseRedirect("/news_curate")
    else:
        form=UserForm()
    return render(request, 'news_curate/signup.html', {"form":form})
"""

""" 
# 로그인
def signin_view(request): 
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
                user_match_with_id = User.objects.filter(id=request.POST['id']).first()
                if user_match_with_id == None :
                    print("ID Wrong !! ==>  ID  :", request.POST['id'])
                    return HttpResponseRedirect("/news_curate/signin")
                
                if  user_match_with_id.pwd == request.POST['pwd']:
                        print("==> LOGIN SUCCESS ==>  ID  :", user_match_with_id.id)
                        return HttpResponseRedirect("/news_curate/")
                else:
                        print("==> PW Wrong !! ==>  ID  :", user_match_with_id.id)
                        return HttpResponseRedirect("/news_curate/signin")
    else:
        form=LoginForm()
    return render(request, 'news_curate/signin.html', {"form":form})
 """
"""     
def test_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            print(form)
            return HttpResponseRedirect("/news_curate")
    else :
        form = NameForm()
    return render(request, "news_curate/name.html", {"form" : form})
 """
from django.views.generic import ListView, DetailView
from .models import  Article, UserForm , User
from .custom_forms import NameForm, LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView, CreateView

# 뉴스 리스트 뷰
class ArticleListView(ListView): 
    model = Article
    queryset=Article.objects.order_by('-published_date').exclude(published_date = None )
    paginate_by = 100
    template_name = 'news_curate/article_list.html'

# 뉴스 상세페이지 뷰
class ArticleDetailView(DetailView): 
    model= Article
    template_name ='news_curate/detail.html' 
    context_object_name = 'article'
    
#회원가입 뷰
class UserCreateView(CreateView):
    model = User
    fields='__all__'
    success_url='/news_curate/'
    template_name='news_curate/signup.html'

#로그인 뷰
class LoginView(FormView):
    template_name = 'news_curate/signin.html'
    form_class = LoginForm
    success_url = '/news_curate/'

    def form_valid(self, form):
        print("== Form is Valid ! == ")
        val = form.validate()
        if val == False :
            self.success_url =  '/news_curate/signin'       
        return super().form_valid(form)
           
    


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
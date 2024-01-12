
from typing import Any
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render , get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import  Article
from django.utils import timezone
# Create your views here.
class ArticleListView(ListView):
    print("== ArticleListView Rendering == ")
    model = Article
    paginate_by = 100
    
""" 
class ArticleDetailView(DetailView):
    print("== ArticleDetailView Rendering == ")
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] =  timezone.now()
        return context  """
        
def ArticleDetailView(request, news_slug):
    try:
        article = get_object_or_404(Article , slug=news_slug)
        
        print("Detail Page Article : ", article)
    except Article.DoesNotExist :
        raise Http404("Article Does Not Exist")
    return render(request, 'news_curate/detail.html',{'article':article})
    # sample slug : 2023-12-20-tech-christmas-shipping-deadlines-ups-usps-fedex  
  

class ArticleDetailUsingDetailView(DetailView):
    model= Article.objects.filter(slug=slug_url_kwarg)
    template_name ='news_curate/detail.html' 
    context_object_name = 'article'
    

    

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView
from .models import  Article
# Create your views here.
class ArticleListView(ListView):
    print("Index View Rendering")
    try:
        queryset=Article.objects.all()
        print("queryset : ", queryset)
        context_object_name  = 'cnn_articles'
        template_name = 'article_list.html'
        """ queryset= Article.objects.order_by('-pub_date')[:5]
        template_name = 'news_curate/index.html'
        context_object_name = 'latest_question_list' """
    except Exception as e :
        print("Error : ", e)
        
""" class DetailView(generic.DetailView):
    model = Question
    template_name = 'news_curate/detail.html'
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'news_curate/results.html'
 """    

""" def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("new_curate/index.html")

    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, 'new_curate/index.html' , context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "new_curate/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
 """

""" def vote(request, question_id):
    question = get_object_or_404(Question , pk=question_id)
    try :
        selected_choice  = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError , Choice.DoesNotExist):
        return render(
            request,
            "new_curate/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("new_curate:results", args=(question.id,)))
    
 """
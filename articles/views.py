from django.http import request
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):

    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

def article_details(request,slug_thing):
    # return HttpResponse(slug_thing)
    article = Article.objects.get(slug=slug_thing)
    return render(request,'articles/article_details.html',{'article':article})

@login_required(login_url='accounts:signin')
def create_article(request):
    return render(request,'articles/create_article.html')

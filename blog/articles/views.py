
# Create your views here.
from .models import Article
from django.shortcuts import render
from django import template
from django.http import Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        print("DEBUG found:", post.title)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        print("DEBUG not found, count =", Article.objects.count())
        raise Http404

from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


def index(requests):
    #return HttpResponse('HELLO')
    posts = Posts.objects.all()[:20]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(requests, 'posts/index.html', context)

def details(requests, id):
    post = Posts.objects.get(id=id)
    context = {
        'post' : post
    }
    return render(requests, 'posts/details.html', context)


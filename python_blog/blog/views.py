from django.shortcuts import render

# Create your views here.
from blog.models import Post, Contact


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def news(request):
    import requests
    import json

    news_api_request = requests.get(
        'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=759a41ef0f944f91a5939ea831376dd8')

    api = json.loads(news_api_request.content)

    return render(request, 'blog/news.html', {'api': api})


def contactUsers(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'blog/contact_final.html')
    return render(request, 'blog/contact.html')

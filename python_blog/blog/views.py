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
    return render(request, 'blog/news.html')


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

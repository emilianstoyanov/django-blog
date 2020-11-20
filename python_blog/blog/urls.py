from django.urls import path

from blog.views import home, about

urlpatterns = [
    path('', home, name='home-page'),
    path('about/', about, name='about-page'),

]

from django.urls import path

from blog import views
from blog.views import home, about

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),

]

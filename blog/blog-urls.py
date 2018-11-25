from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('<slug:slug>', views.page, name='page'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('post/<slug:slug>/', views.post, name='post')
]

from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name ='article_list'),
    path('<str:slug_thing>/',views.article_details,name='details')
    ]

urlpatterns += staticfiles_urlpatterns()

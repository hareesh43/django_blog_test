from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.article_list)
    ]

urlpatterns += staticfiles_urlpatterns()

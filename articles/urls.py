from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name ='article_list'),
    path('create/',views.create_article,name='create'),
    path('<str:slug_thing>/',views.article_details,name='details')
    ]
# for static files

urlpatterns += staticfiles_urlpatterns()

#for media files
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


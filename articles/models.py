from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 20)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    #add author
    thumb = models.ImageField(default='default.png',blank=True)
    

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50]+'...'
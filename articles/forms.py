from django import forms
from django.forms import fields
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','body','slug','thumb']
          
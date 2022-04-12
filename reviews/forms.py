
from django import forms
from django.contrib.auth.models import User
from .views import Post



class CrearPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','body','calificacion']
        help_texts = {k:'' for k in fields }



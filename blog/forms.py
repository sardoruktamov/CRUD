from django.forms import ModelForm
from .models import Blog
from django import forms

class BlogCreatForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'sana']
        labels = {'title':'Title' ,'sana':'sana'}
        widgets = {'title':forms.TextInput(attrs={'class':'ml-2'}),
                    'sana':forms.TextInput(attrs={'class':'ml-2'})
                  }
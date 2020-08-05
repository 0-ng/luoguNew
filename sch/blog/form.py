from django import forms
from .models import Article
from mdeditor.fields import MDTextFormField

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("body", )
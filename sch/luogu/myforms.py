from django import forms
from .models import Question, Note
from mdeditor.fields import MDTextFormField

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("body", )



class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question", "answer")


from django import forms
from .models import Comment


# Criando o formulário apenas usando o form do django
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


# Criando um formulário dinamicamente usando a classe especifica e ModelForm do django
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

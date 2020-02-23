from django import forms

from blog.models import Post, Comment

"""импортирую модуль с формами из стандартной библиотеки джанги"""
"""Каждой отображаемой модели должна соответствовать форма в этом файле"""


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

"""Создаю новый класс с  формой для класса Post"""

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


""" this is own created form that provide ability to send article
and share them using only email. Form is real form in the straight sense,
can be filled by anything"""

class PostSendForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
from django import forms

from blog.models import Post, Comment

"""импортирую модуль с формами из стандартной библиотеки джанги"""
"""Каждой отображаемой модели должна соответствовать форма в этом файле"""


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'slug',)

"""Создаю новый класс с  формой для класса Post"""

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


from django import forms

from blog.models import Post

"""импортирую модуль с формами из стандартной библиотеки джанги"""

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

"""Создаю новый класс с  формой для класса Post"""
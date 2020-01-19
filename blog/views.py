from django.shortcuts import render

# Create your views here.

"""Первое представление, которое принимает запрос в качестве аргумента
и рендерит страницу с постами (создаёт шаблон)"""
def post_list(request):
    return render(request, 'blog/post_list.html', {})

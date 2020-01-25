from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

""" Первое представление, которое принимает запрос в качестве аргумента
и рендерит страницу с постами (передаёт в шаблоны templates) """
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

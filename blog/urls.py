"""Так импортируются все view из блога"""

from django.urls import path
from . import views

"""Вот эта штука называется url-шаблон, добавляется ручками"""
"""Таким образом мы связываем view под именем 'post_list' с корневым адресом"""
urlpatterns = [
    path('', views.post_list, name='post_list'), #'' - этот шаблон соответствует пустой строке
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  
]
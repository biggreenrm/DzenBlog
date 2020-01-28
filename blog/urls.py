"""Так импортируются все view из блога"""

from django.urls import path
from . import views

"""Вот эта штука называется url-шаблон, добавляется ручками"""
"""Таким образом мы связываем view под именем 'post_list' с корневым адресом"""
urlpatterns = [
    path('', views.post_list, name='post_list'), #'' - этот шаблон соответствует пустой строке
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  
]
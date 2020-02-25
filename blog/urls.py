"""Так импортируются все view из блога"""

from django.urls import path
from . import views

"""Вот эта штука называется url-шаблон, добавляется ручками"""
"""Таким образом мы связываем view под именем 'post_list' с корневым адресом"""
urlpatterns = [
    path('', views.post_list, name='post_list'), #'' - этот шаблон соответствует пустой строке
    path('theory/', views.post_list_theory, name='post_list_theory'),
    path('practice/', views.post_list_practice, name='post_list_practice'),
    path('poetry/', views.post_list_poetry, name='post_list_poetry'),
    path('mindflow/', views.post_list_mindflow, name='post_list_mindflow'),
    path('post/<slug>/', views.post_detail, name='post_detail'),
    path('post/<slug>/share/', views.post_share, name='post_share'),
    path('new/', views.post_new, name='post_new'),
    path('post/<slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug>/remove/', views.post_remove, name='post_remove'),
    path('post/<slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<slug>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<slug>/remove/', views.comment_remove, name='comment_remove'),
]
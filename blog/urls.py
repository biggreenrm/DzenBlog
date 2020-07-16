"""Так импортируются все view из блога"""

from django.urls import path
from . import views
from .feeds import PostFeed


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<theme>", views.post_list_theme, name="post_list_theme"),
    path(
        "post/<int:year>/<int:month>/<int:day>/<id>/",
        views.post_detail,
        name="post_detail",
    ),
    path("post/<id>/share/", views.post_share, name="post_share"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    path("new/", views.post_new, name="post_new"),
    path("post/<id>/edit/", views.post_edit, name="post_edit"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<id>/publish/", views.post_publish, name="post_publish"),
    path("post/<id>/remove/", views.post_remove, name="post_remove"),
    path("post/<id>/comment/", views.add_comment_to_post, name="add_comment_to_post"),
    path("comment/<id>/approve/", views.comment_approve, name="comment_approve"),
    path("comment/<id>/remove/", views.comment_remove, name="comment_remove"),
    path("api/post/", views.PostView.as_view(), name="post_list_api"),
    path("api/post/<id>/", views.PostView.as_view(), name="post_detail_api"),
    path("search/", views.post_search, name="post_search"),
    path("feed/", PostFeed(), name="post_feed"),
]

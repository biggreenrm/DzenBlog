from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .models import LikeDislike
from blog.models import Post, Comment

app_name = "ajax"
urlpatterns = [
    url(
        r"api/post/(?P<id>\d+)/like/$",
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name="post_like",
    ),
    url(
        r"api/post/(?P<id>\d+)/dislike/$",
        login_required(
            views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)
        ),
        name="post_dislike",
    ),
    url(
        r"api/comment/(?P<id>\d+)/like/$",
        login_required(
            views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)
        ),
        name="comment_like",
    ),
    url(
        r"api/comment/(?P<id>\d+)/dislike/$",
        login_required(
            views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)
        ),
        name="comment_dislike",
    ),
]

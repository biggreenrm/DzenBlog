from django.shortcuts import render
from .serializers import PostSeriazizer
from .models import Post, Comment
from .templates.blog.forms import PostForm, CommentForm, PostSendForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from autoslug import AutoSlugField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
""" Функция пагинатор, написанная для того, чтобы не раздувать каждое представление,
заменяя 16 строк кода всего одной. DRY """
def paginate(posts, request, num):
    paginator = Paginator(
        posts, num
    )  # создаём пагинатор (разбиение на страницы), по 3 поста на страничку
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
        return posts
    except PageNotAnInteger:
        # if page is not number - return first page
        posts = paginator.page(1)
        return posts
    except EmptyPage:
        return posts
        posts = paginator.page(paginator.num_pages)
        # if number is more, than total amount of pages - return last
    

class PostView(APIView):
    """PostView instead of simple def post-list()"""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSeriazizer(posts, many=True)
        return Response({'posts': serializer.data})
    
    def post(self, request):
        post_article = request.data.get('post_article')
        serializer = PostSeriazizer(data=post_article)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})
    
    def put(self, request, slug):
        saved_post = get_object_or_404(Post.objects.all(), slug=slug)
        data = request.data.get('post_article')
        serializer = PostSeriazizer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(post_saved.title)})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    posts = paginate(posts, request, 3)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_list_theme(request, theme):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    posts = posts.filter(theme=theme)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by("created_date")
    return render(request, "blog/post_draft_list.html", {"posts": posts})


@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect("post_detail", slug=slug)


@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("post_list")


def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment_to_post.html", {"form": form})


@login_required
def comment_approve(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    comment.approve()
    return redirect("post_detail", slug=comment.post.slug)


@login_required
def comment_remove(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    comment.delete()
    return redirect("post_detail", slug=comment.post.slug)


def post_share(request, slug):
    post = get_object_or_404(Post, slug=slug)
    sent = False
    if request.method == "POST":
        form = PostSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            post_url = request.build_absolute_uri(post.slug)
            subject = '{} ({}) recommends you reading "{}"'.format(
                cd["name"], cd["email"], post.title
            )
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(
                post.title, post_url, cd["name"], cd["comments"]
            )
            send_mail(subject, message, "biggreen.rm@gmail.com", [cd["to"]])
            sent = True
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostSendForm()
        return render(
            request, "blog/share.html", {"post": post, "form": form, "sent": sent}
        )

from django.contrib import admin
from .models import Post, Comment
from user.models import CustomUser

# Register your models here.

# add model comment to the admin panel at "admin/"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text", "created_date", "approved_comment")
    list_filter = ("post", "author", "text", "created_date", "approved_comment")
    search_fields = ("text",)
    ordering = ("created_date", "author")


# этот декоратор выполняет ту же самую функцию, что и admin.site.register(Post)
# параметр list_display указывает джанге какие поля выводить в админке
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "theme",
        "published_date",
        "created_date",
    )
    list_filter = (
        "created_date",
        "published_date",
        "author",
        "theme",
    )  # add filter to the right (created, published date) and
    # possibility to sort list in admin panel
    search_fields = (
        "title",
        "text",
    )  # add search field to the top to make search in 'text' and 'title' columns of DB.
    prepopulated_fields = {"slug": ("title",)}  # auto-generating urls from title
    date_hierarchy = "created_date"  # add date navigation panel
    ordering = ("created_date", "author")  # default sorting style
    """Все переменные выше уже знакомы джанге и именно по ним она ориентируется)"""


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_staff", "last_login")
    list_filter = ("first_name", "last_name", "email", "is_staff", "last_login")
    ordering = ("last_name",)
    search_fields = ("first_name", "last_name")

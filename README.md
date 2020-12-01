# DzenToday Blog

DzenBlog is a web-application built with python and Django Framework. It has not stricted subject, and created, most of all, with aim to learn how to do such kind of applications. Main features of DzenBlog: rich text (WYSIWYG) redactor for posts, comment and like/dislike systems (AJAX/JS), search and tag system, sharing by e-mail. DzenBlog also has API (Django Rest Framework) providing an opportunity to work with article models.


## Installation

Simply clone the repo and install requirements
```
pip install -r requirements.txt
```

You also have to create private_settings.py file in the same folder with settings.py, in which will be placed next settings:
```
#SMTP-settings for sharing articles by email
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = ''

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
```


## Features

**Main page** is shown below. It provides menu with article topics, big jumbotron, buttons for login/logout, search and add post. There is also the possibility to subscribe via RSS.
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/main_screen_above.png)

There is two main articles, that can be shown separately on the top in boxes. And after it - list of articles with common information: likes, comments, author, date/time of publication. Area with tags shown is shown on the right.
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/main_screen_below.png)

On the bottom - pagination:
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/main_screen_bottom.png)



**Post redactor WYSIWIG** is built in application. It gives an opportunity to write not simple text, but to use rich text format (change size, color and etc.). Redactor is available from the page of creating post:
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/new_post_redactor.png)

And from admin panel too:
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/admin_panel_post.png)


**Like/dislike and comment system** is based on Redis in order to optimize usage of database. It is good practice to put in Redis amount of likes/dislikes for every post instead of calculating them each time.
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/post_like_comment.png)


**Search page** is shown below. Search engine - postgres.search (SearchVector, SearchQuery, SearchRank).
![alt text](https://github.com/biggreenrm/DzenBlog/blob/master/readme_screenshots/search.png)


**Django Rest Framework** is also used in this projects. It provides ability of using CRUD functions to affect article model.


## Tech-stack

Django, Django Rest Framework, Redis, PostgreSQL, TinyMCE, SMTP.

## Project status

Stopped for a while.
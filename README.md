# DzenToday Blog
This is a blog build with Python and Django, aimed to show the opportunities gived by this tools. 

## Summary
This blog provides users with the opportunity to be authorized, write articles using WYSIWYG rich text redactor built in application, also write comments and
like/dislike them (articles too, of course). Like/dislike system works on AJAX with JS, so pages don't need to be refreshed to see results. All articles has its tags. 
I also made an RSS for users that want to read articles in RSS-reader, and share system using e-mail.
DzenToday blog have API (Django REST) to workwith article model. Users can use built-in search system to find certain articles. URL-adressess bases on slugs easy to read.
Also I used Django-crispy-forms to make forms looks pretty (pretty for backend developer :) and Django-inline-svg to place icons in template.

## Technologies
- django==2.2.12
- djangorestframework==3.11.0

  CRU without D - Articles can be showed, updated and created through API based on JSON.
  
- Redis

  Redis used to work with like/dislike system because it counts such kind of information much faster than any Relational Database.
  
 - django-tinymce==3.0.2
 
    TinyMCE provides tool to write text in rich html format (WYSIWYG), so users can make posts with pretty good formatting and put images in it.
  
 - django-taggit==1.3.0
 - django-inline-svg==0.1.1
 - PostgreSQL
  
    For such kind of application there is no big difference between databases, so you can choose any you want.
    
  ## Instalation
  Simple as it can be. Just set up venv and install requirements.


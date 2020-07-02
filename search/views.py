from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from blog.models import Post

# Create your views here.

class ESearchView(View):
    template_name = 'blog/search.html'
    
    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_posts = Post.objects.filter(text__search=question)
            context['last_question'] = '?q=%s' % question
            # Руководствуясь DRY здесь можно было бы сделать пагинацию
            # импортированную из blog.views и сделать аналогично
            current_page = Paginator(search_posts, 10)

            page = request.GET.get('page')
            try:
                context['post_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['post_lists'] = current_page.page(1)
            except EmptyPage:
                context['post_lists'] = current_page.page(current_page.num_pages)
        #import pdb; pdb.set_trace()
        return render(request, template_name=self.template_name, context=context)
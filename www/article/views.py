# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from django.conf import settings

from article.models import Article

PAGINATE_BY = getattr(settings, 'ARTICLE_PAGINATE_BY', 10)

##########################################################################
##########################################################################

class ArticleMixin(object):
	def get_queryset(self):
		return Article.activs.all()
		
	def get_context_data(self, **kwargs):
		context = super(ArticleMixin, self).get_context_data(**kwargs)
		context.update({'active':'article'})
		return context
		
##########################################################################
##########################################################################

class ArticleList(ArticleMixin, ListView):
	paginate_by = PAGINATE_BY
	template_name = 'article/list.html'
	context_object_name = 'article_list'
	
##########################################################################
##########################################################################
	
class ArticleView(ArticleMixin, DetailView):
	template_name = 'article/article.html'
	
##########################################################################
##########################################################################
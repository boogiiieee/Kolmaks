# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from portfolio.models import Product

##########################################################################
##########################################################################

class PortfolioMixin(object):
	def get_context_data(self, **kwargs):
		context = super(PortfolioMixin, self).get_context_data(**kwargs)
		context.update({'active':'portfolio',})
		return context
		
	def get_queryset(self):
		return Product.activs.all()
		
##########################################################################
##########################################################################

class ProductList(PortfolioMixin, TemplateView):
	template_name = 'portfolio/list.html'
	
	def get_context_data(self, **kwargs):
		context = super(ProductList, self).get_context_data(**kwargs)
		context['product_list'] = Product.activs.all().order_by('-year')
		return context
	
##########################################################################
##########################################################################

class ProductItem(PortfolioMixin, DetailView):
	template_name = 'portfolio/product.html'
	context_object_name='product'
	
##########################################################################
##########################################################################
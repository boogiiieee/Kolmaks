# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from catalog.models import Product
from catalog.conf import settings as conf
		
##########################################################################
##########################################################################

class CatalogMixin(object):
	def get_context_data(self, **kwargs):
		context = super(CatalogMixin, self).get_context_data(**kwargs)
		context.update({'active':'catalog',})
		return context
		
##########################################################################
##########################################################################

class ProductList(CatalogMixin, ListView):
	paginate_by = conf.PAGINATE_BY
	template_name = 'catalog/catalog.html'
	context_object_name = 'product_list'
	slug_url_kwarg = 'slug'

	def get_queryset(self):
		return Product.activs.all()
		
	def get_context_data(self, **kwargs):
		context = super(ProductList, self).get_context_data(**kwargs)
		return context
	
##########################################################################
##########################################################################

class ProductItem(CatalogMixin, DetailView):
	template_name = 'catalog/product.html'
	context_object_name='product'
	
	def get_queryset(self):
		return Product.activs.all()
		
	def get_context_data(self, **kwargs):
		context = super(ProductItem, self).get_context_data(**kwargs)
		return context
	
##########################################################################
##########################################################################
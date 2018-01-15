# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap

from catalog.models import Product

##########################################################################
##########################################################################

#Для карты сайта
	
class ProductSitemap(Sitemap):
	def items(self):
		return Product.activs.all()
		
	def location(self, obj):
		return obj.get_absolute_url()
		
##########################################################################
##########################################################################
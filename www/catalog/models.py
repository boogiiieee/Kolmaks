# -*- coding: utf-8 -*-

from django.db import models
import os

from pytils.translit import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField as SorlImageField

		
##########################################################################
##########################################################################

class ProductManager(models.Manager): 
	def get_query_set(self): 
		return super(ProductManager, self).get_query_set().filter(is_active=True)

class Product(models.Model):	
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/catalog/product/%s' % filename.lower()
		
	title = models.CharField(max_length=100, verbose_name=u'название')
	slug = models.SlugField(max_length=500, verbose_name=u'псевдоним', unique=True)
	text = RichTextField( verbose_name=u'текст', blank=True, null=True)
	
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	description = models.TextField(u'описание', blank=True)
	keywords = models.TextField(u'ключевые слова через запятую', blank=True)
	
	object = models.Manager()
	activs = ProductManager()
	
	def get_title(self): return self.title
	def get_text(self): return self.text
	def get_description(self): return self.description
	def get_keywords(self): return self.keywords
	
	def __unicode__(self):
		return u'%s' % self.get_title()
		
	@models.permalink
	def get_absolute_url(self):
		return ('product_url', (), {'slug':self.slug})
		
	def get_admin_url(self):
		return u'/admin/catalog/product/%d/' % self.id

	class Meta: 
		verbose_name = u'товар'
		verbose_name_plural = u'товары'
		ordering = ['sort', '-id']
	
##########################################################################
##########################################################################
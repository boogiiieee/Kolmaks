# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
import re, os

from pytils.translit import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField as SorlImageField

##########################################################################
##########################################################################

class ActiveManager(models.Manager): 
	def get_query_set(self): 
		return super(ActiveManager, self).get_query_set().filter(is_active=True)
		
##########################################################################
##########################################################################

class Product(models.Model):	
	title = models.CharField(max_length=100, verbose_name=u'название')
	slug = models.SlugField(max_length=500, verbose_name=u'псевдоним', unique=True)
	text = RichTextField(verbose_name=u'текст', blank=True, null=True)
	year = models.IntegerField(verbose_name=u'год')
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	description = models.TextField(u'описание', blank=True)
	keywords = models.TextField(u'ключевые слова через запятую', blank=True)
	
	objects = models.Manager()
	activs = ActiveManager()
	
	def get_title(self): return self.title
	def get_text(self): return self.text
	def get_year(self): return self.year
	def get_description(self): return self.description
	def get_keywords(self): return self.keywords
	
	def __unicode__(self):
		return u'%s' % self.get_title()
		
	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_item_url', (), {'slug':self.slug})
		
	def get_admin_url(self):
		return reverse('admin:%s_%s_change' % (self._meta.app_label,  self._meta.module_name),  args=[self.id] )
		
	def get_images(self):
		return self.productgallery_set.filter(is_active=True)
		
	def get_image(self):
		images = self.get_images()
		if images:
			try:
				return images.get(is_main=True).image
			except:
				return images[0].image
		return None
	
	class Meta: 
		verbose_name = u'товар'
		verbose_name_plural = u'товары'
		ordering = ['sort', '-id']
	
##########################################################################
##########################################################################

class ProductGallery(models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/portfolio/%s' % filename.lower()
		
	product = models.ForeignKey(Product, verbose_name=u'товар')
	image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение')
	is_main = models.BooleanField(verbose_name=u'главное', default=False)
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	objects = models.Manager()
	activs = ActiveManager()
	
	def get_title(self): return self.image.url
	def get_image(self): return self.image
	
	def __unicode__(self):
		return self.get_title()
		
	class Meta: 
		verbose_name = u'изображение' 
		verbose_name_plural = u'галерея'
		ordering = ['sort', '-id']
		
	def save(self, *args, **kwargs):
		if self.is_main:
			ProductGallery.objects.filter(product=self.product, is_main=True).update(is_main=False)
		super(ProductGallery, self).save(*args, **kwargs)
		
##########################################################################
##########################################################################
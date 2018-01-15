# -*- coding: utf-8 -*-

from django.db import models
import os

from pytils.translit import slugify
from sorl.thumbnail import ImageField as SorlImageField
from ckeditor.fields import RichTextField

################################################################################################################
################################################################################################################

class PartnerManager(models.Manager): 
	def get_query_set(self): 
		return super(PartnerManager, self).get_query_set().filter(is_active=True)
		
class Partner(models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/partners/%s' % filename.lower()
		
	title = models.CharField(max_length=100, verbose_name=u'заголовок')
	image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение')	
	url = models.URLField(max_length=100, blank=True)
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	activs = PartnerManager()
	
	def get_title(self): return self.title
	def get_image(self): return self.image
	def get_url(self): return self.url
          
	def __unicode__(self):
		return self.get_title()
     
	class Meta:
		verbose_name = u'партнер'
		verbose_name_plural = u'партнеры'
		ordering = ['sort', '-id']
		
################################################################################################################
################################################################################################################
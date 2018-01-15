# -*- coding: utf-8 -*-

from django.db import models

from ckeditor.fields import RichTextField

################################################################################################################
################################################################################################################

class OrderItem(models.Model):
	org = models.CharField(max_length=100, verbose_name=u'организация')
	name = models.CharField(max_length=100, verbose_name=u'контактное лицо')
	phone = models.CharField(max_length=100, verbose_name=u'телефон', blank=True)
	email = models.CharField(max_length=100, verbose_name=u'e-mail')	
	msg = RichTextField(max_length=1000, verbose_name=u'характеристики выбранного товара')
	created_at = models.DateTimeField(verbose_name=u'дата создания', auto_now_add=True)
	
	def get_org(self): return self.org
	def get_name(self): return self.name
	def get_email(self): return self.email
	def get_phone(self): return self.phone
	def get_msg(self): return self.msg
	def get_created_at(self): return self.created_at
	
	def __unicode__(self):
		return u'%s' % self.get_org()
		
	class Meta: 
		verbose_name = u'заказ' 
		verbose_name_plural = u'заказы клиентов'
		ordering = ['-created_at', '-id']
		
################################################################################################################
################################################################################################################
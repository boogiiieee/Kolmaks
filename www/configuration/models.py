# -*- coding: utf-8 -*-

from django.db import models

from map2gis.django_2gis_widget import LocationField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^map2gis\.django_2gis_widget\.LocationField"])

#######################################################################################################################
#######################################################################################################################

#Настройки
class ConfigModel(models.Model):
	title = models.CharField(max_length=100, verbose_name=u'название сайта', default=u'Название сайта')	
	
	is_active_map_1 = models.BooleanField(verbose_name=u'показывать карту офиса', default=True)
	address1 = LocationField(verbose_name=u'адрес офиса', blank=True, null=True)
		
	is_active_map_2 = models.BooleanField(verbose_name=u'показывать карту склада', default=True)
	address2 = LocationField(verbose_name=u'адрес склада', blank=True, null=True)
	
	def __unicode__(self):
		return u'настройки'
		
	class Meta: 
		verbose_name = u'настройки' 
		verbose_name_plural = u'настройки'

#######################################################################################################################
#######################################################################################################################
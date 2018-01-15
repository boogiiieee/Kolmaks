# -*- coding: utf-8 -*-

from django.contrib import admin

from configuration.models import ConfigModel
from configuration.forms import ConfigForm

##########################################################################
##########################################################################

class ConfigModelAdmin(admin.ModelAdmin):
	form = ConfigForm
	list_display = ('title', 'is_active_map_1', 'is_active_map_2')
	list_editable = ('is_active_map_1', 'is_active_map_2')
	fieldsets = (
		(None, {'fields': ('title',)}),
        (u'Карта', {'fields': ('is_active_map_1', 'address1', 'is_active_map_2', 'address2') }),
	)
	
	def has_add_permission(self, *args, **kwargs):
		return False
		
	def has_delete_permission(self, *args, **kwargs):
		return False
	
admin.site.register(ConfigModel, ConfigModelAdmin)

##########################################################################
##########################################################################
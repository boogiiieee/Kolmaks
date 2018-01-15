# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from catalog.models import Product

##########################################################################
##########################################################################
	
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('title', 'is_active', 'sort')
	list_filter = ('is_active',)
	list_editable = ('is_active', 'sort')
	prepopulated_fields = {"slug": ("title",),}
	fieldsets = (
		(None, {'fields': ('title', 'slug', 'text', 'is_active', 'sort')},),
		(u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
	)
	
admin.site.register(Product, ProductAdmin)

##########################################################################
##########################################################################
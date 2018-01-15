# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from portfolio.models import Product, ProductGallery

##########################################################################
##########################################################################

class ProductGalleryInline(AdminImageMixin, admin.TabularInline):
	model = ProductGallery
	
class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductGalleryInline,]
	list_display = ('title', 'slug', 'year', 'is_active', 'sort')
	list_filter = ('is_active', 'year')
	list_editable = ('is_active', 'sort')
	prepopulated_fields = {"slug": ("title",),}
	fieldsets = (
		(None, {'fields': ('title', 'slug', 'text', 'year', 'is_active', 'sort')},),
		(u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
	)
	
admin.site.register(Product, ProductAdmin)

##########################################################################
##########################################################################
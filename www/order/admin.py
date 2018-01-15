# -*- coding: utf-8 -*-

from django.contrib import admin

from order.models import OrderItem

################################################################################################################
################################################################################################################

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('org', 'name', 'phone', 'email', 'created_at')
	list_filter = ('created_at',)
	fieldsets = (
		(None, {'fields': ('org', 'name', 'phone', 'email',  'msg')},),
	)
	
admin.site.register(OrderItem, OrderItemAdmin)

################################################################################################################
################################################################################################################
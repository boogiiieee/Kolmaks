# -*- coding: utf-8 -*-

from django.conf.urls import *

from portfolio.views import ProductList, ProductItem

urlpatterns = patterns('portfolio.views',
	url(r'^$', ProductList.as_view(), name='portfolio_list_url'),
	url(r'^(?P<slug>[-_\w]+)/$', ProductItem.as_view(), name='portfolio_item_url'),
)
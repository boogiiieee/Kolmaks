# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from order.views import OrderView

urlpatterns = patterns('order.views',
	url(r'^$', OrderView.as_view(), name='order_url'),
)
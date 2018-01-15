# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from feedback.views import FeedbackView

urlpatterns = patterns('feedback.views',
	url(r'^$', FeedbackView.as_view(), name='feedback_url'),
)
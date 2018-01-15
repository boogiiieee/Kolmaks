# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from article.sitemap import ArticleSitemap
from catalog.sitemap import ProductSitemap


sitemaps = {
	'flatpages': FlatPageSitemap,
	'product': ProductSitemap,
	'article': ArticleSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin_tools/', include('admin_tools.urls')),
	
	url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^captcha/', include('captcha.urls')),

	url(r'^news/', include('article.urls')),
	url(r'^catalog/', include('catalog.urls')),
	url(r'^order/', include('order.urls')),
	url(r'^contacts/', include('feedback.urls')),
	
	url(r'^robots\.txt$', include('robots.urls')),
	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),	
	
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
)

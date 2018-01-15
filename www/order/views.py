# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.views.generic.edit import FormView
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_managers

from order.models import OrderItem
from order.forms import OrderForm

################################################################################################################
################################################################################################################

class OrderView(FormView):
	form_class = OrderForm
	success_url = reverse_lazy('order_url')
	template_name = 'order_form.html'
	
	def get_context_data(self, **kwargs):
		context = super(OrderView, self).get_context_data(**kwargs)
		context.update({'active':'order',})
		return context
	
	def form_valid(self, form):
		q = form.cleaned_data
		q.pop('captcha', None)
		item = OrderItem.objects.create(**q)
			
		domain = Site.objects.get_current().domain
		
		subject = u'Новый заказ на сайте %s' % domain
		
		t = get_template('mail/order_mail.html') 
		message = t.render(Context({'item':item, 'domain':domain}))
		
		mail_managers(subject, message, html_message=message)
		
		messages.add_message(self.request, messages.INFO, u'Спасибо, Ваш заказ отправлен!')
		return HttpResponseRedirect(self.get_success_url())
	
################################################################################################################
################################################################################################################
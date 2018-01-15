# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
import cgi
import re

from order.models import OrderItem

################################################################################################################
################################################################################################################

class OrderForm(forms.ModelForm):
	msg = forms.CharField(label=u'Характеристики выбранного товара', max_length=1000, widget=forms.Textarea(attrs={'rows':"4",}))
	captcha = CaptchaField(label=u'Код защиты')
	
	class Meta:
		model = OrderItem
		fields = ('org', 'name', 'phone', 'email', 'msg', 'captcha')
		
	def clean_org(self): 
		org = self.cleaned_data['org']
		if len(org) < 2:
			raise forms.ValidationError(u'Слишком короткое название организации')
		return org
		
	def clean_name(self): 
		name = self.cleaned_data['name']
		if len(name) < 3:
			raise forms.ValidationError(u'Слишком короткое ФИО')
		return name
		
	def clean_email(self): 
		email = self.cleaned_data['email']
		if email:
			r = re.compile('^[0-9a-zA-Z]+[-\._0-9a-zA-Z]*@[0-9a-zA-Z]+[-\._^0-9a-zA-Z]*[0-9a-zA-Z]+[\.]{1}[a-zA-Z]{2,6}$')
			if not r.findall(email):
				raise forms.ValidationError(u'Некорректный E-mail')
		return email
		
	def clean_phone(self): 
		phone = self.cleaned_data['phone']
		if phone:
			r = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
			if not r.findall(phone):
				raise forms.ValidationError(u'Некорректный номер телефона')
		return phone
		
	def clean_msg(self): 
		msg = self.cleaned_data['msg']
		msg = cgi.escape(msg)
		if len(msg) < 10:
			raise forms.ValidationError(u'Слишком короткое сообщение')
		return msg
		
################################################################################################################
################################################################################################################
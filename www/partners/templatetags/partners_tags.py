# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template

from partners.models import Partner

register = template.Library()

################################################################################################################
################################################################################################################

class get_partners_list_node(Node):
	def render(self, context):
		context['partners_list'] = Partner.activs.all()
		return ''
		
def get_partners_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1:
		raise TemplateSyntaxError(u"%r имеет > 1 аргумента" % bits[0])
	return get_partners_list_node()
	
get_partners_list = register.tag(get_partners_list)

################################################################################################################
################################################################################################################
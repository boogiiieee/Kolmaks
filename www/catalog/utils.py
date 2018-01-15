# -*- coding: utf-8 -*-

import re
from django.utils.encoding import force_unicode

#######################################################################################################################
#######################################################################################################################

def cost_intcomma(value, exploder=' '):
    """
    Converts an integer to a string containing commas every three digits.
    For example, 3000 becomes '3 000' and 45000 becomes '45 000'.
    """
    orig = force_unicode(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>%s\g<2>' % exploder, orig)
    if orig == new: return new
    else: return cost_intcomma(new)
	
#######################################################################################################################
#######################################################################################################################
from django import template
from datetime import date, timedelta

register = template.Library()

#@register.filter(name=cut)
#def cut(value):
#    pass

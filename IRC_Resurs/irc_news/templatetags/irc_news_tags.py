from django import template
from irc_news.models import *


register = template.Library()

@register.simple_tag()
def get_news():
    return News.objects.all()
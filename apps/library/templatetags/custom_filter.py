import random
from django import template
register = template.Library()


@register.filter
def shuffle(arg):
    temp = list(arg)[:]
    random.shuffle(temp)
    return temp

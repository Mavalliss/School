from django import template
from basics.models import Urgent

register = template.Library()


@register.simple_tag
def get_announcement():
    try:
        return Urgent.objects.get(pk=1)
    except:
        pass

from django import template
from basics.models import Urgent

register = template.Library()


@register.simple_tag
def get_announcement():
    try:
        return Urgent.objects.order_by('-id')[0]  # Последняя важная статья
    except:
        pass

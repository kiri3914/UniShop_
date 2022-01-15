from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('shop.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}

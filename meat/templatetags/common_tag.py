from django import template

register = template.Library()


@register.simple_tag()
def company(key):
    """
    客户信息标签
    :param key:
    :return:
    """
    from meat.settings import COMPANY
    return COMPANY[key]
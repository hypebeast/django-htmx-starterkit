from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def get_active_class(context, url_to_check: str) -> str:
    request = context["request"]
    if request.get_full_path() == reverse(url_to_check):
        return "underline"
    return ""

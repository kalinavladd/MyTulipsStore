# Мы создаем темплейт тег который будет рендерить нашу форму в футоре
from django import template
from contact.forms import ContactForms

register = template.Library()


@register.inclusion_tag("contact/tags/form.html")
def contact_form():
    return {"contact_form": ContactForms}

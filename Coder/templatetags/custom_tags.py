from django import template

register = template.Library()

@register.simple_tag
def get_attr(obj, attr_name):
    # Usa la función getattr de Python para obtener el valor del atributo y devuelve el resultado
    return getattr(obj, attr_name, None)

@register.filter
def items(value):
    return {k: v for k, v in value.__dict__.items() if not k.startswith('_')}.items()

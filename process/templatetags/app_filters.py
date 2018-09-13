from django import template

register = template.Library()

@register.filter(name='difficulty_name')
def difficulty_name(value):
    if value == 1:
        return "Easy"
    elif value == 2:
        return "Medium"
    elif value == 3:
        return "Hard"
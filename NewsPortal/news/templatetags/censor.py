from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    bad_words = ['bad', 'words']

    if isinstance(value, str):
        for word in bad_words:
            value = value.replace(word, '*' * len(word))
    else:
        raise ValueError('censor filter only works with strings')

    return value

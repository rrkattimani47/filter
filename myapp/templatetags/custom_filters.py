from django import template

register=template.Library()#instance of template library

def is_lower(m):
    for i in m:
        if 'A'<=i<='Z':
            return False
    return True
def is_upper(m):
    for i in m:
        if 'a'<=i<='z':
            return False
    return True
register.filter('is_lower',is_lower)
register.filter('isupper',is_upper)

@register.filter(name='plural')
def plural(n,m):
    if n>1:
        return str(n)+" "+m+'s'
    else:
        return str(n)+' '+m
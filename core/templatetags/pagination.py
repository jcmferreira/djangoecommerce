from django.template import Library

register = Library()


# Para o pagination, através do register.inclusion_tag, sempre que ela for renderizada
# o template informado, pagination.html, será utilizado
@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {
        'paginator': paginator,
        'request': request,
        'page_obj': page_obj,
    }

    # Recuperando as variáveis via GET
    getvars = request.GET.copy()

    # Caso exista a variável page, ela é removida
    if 'page' in getvars:
        del getvars['page']

    # Se ainda existir variáveis, ela é readicionada no fim, com o &
    if len(getvars) > 0:
        context['getvars'] = '&{0}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''

    return context

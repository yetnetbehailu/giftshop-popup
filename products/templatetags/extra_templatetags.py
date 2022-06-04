from django import template

# To register a valid template tag
register = template.Library()


@register.simple_tag(takes_context=True)
def url_transform(context, **kwargs):
    """
    # Defines the custom template tag which preserves the url GET parameters
    # whilst updating GET parameter changes passed along to it.
    """
    # Returns a mutable copy of the original immutable request object
    query = context['request'].GET.copy()
    # Appends other dictionary objects to the mutable QueryDict rather than
    # replacing them
    query.update(kwargs)
    return query.urlencode()

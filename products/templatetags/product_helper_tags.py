from django import template

register = template.Library()

@register.simple_tag
def listing_url(value, field_name, url_encode=None):
    """Determines the query strings used to keep
     filters and pagination working on products page"""
    
    url = '?{0}={1}'.format(field_name, value)

    if url_encode:
        querystring = url_encode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url


# code snippet taken from https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html by Vitor Freitas
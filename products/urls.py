from django.conf.urls import url, include
from .views import return_products, product_detail, create_comment
from django.views import static
from trips.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', return_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^comment/(?P<pk>\d+)$', create_comment, name='create_comment'),
    
]
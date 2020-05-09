from django.conf.urls import url, include
from .views import return_products
from django.views import static
from trips.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', return_products, name='products'),
    
]
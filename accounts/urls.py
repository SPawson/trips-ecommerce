from django.conf.urls import url, include
from .views import register

urlpatterns = [
    url(r'^register/$', register, name='register'),
]
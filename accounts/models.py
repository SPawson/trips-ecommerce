from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.utils import timezone

#User model
class User(AuthUser):
    class Meta:
        proxy = True
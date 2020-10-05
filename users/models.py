import uuid
from django.contrib.auth.models import AbstractUser
from localflavor.us.us_states import STATE_CHOICES

from django.db import models

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    user_type = models.CharField(max_length=10,default='',null=True,blank=True)
    user_street_addr = models.CharField(max_length=255,default='',null=True,blank=True)
    user_city = models.CharField(max_length=255,default='',null=True,blank=True)
    user_state = models.CharField(choices=STATE_CHOICES,max_length=2,default='',null=True,blank=True)
    user_zip = models.IntegerField(null=True,blank=True)
    user_organization = models.CharField(max_length=255,null=True,blank=True)
    user_phone = models.CharField(max_length=10,null=True,blank=True)
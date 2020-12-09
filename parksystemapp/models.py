import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.db import models
from django.urls import reverse

class Park(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    park_name = models.CharField(max_length=255,blank=False,null=False,default='')
    park_addr = models.CharField(max_length=255,blank=False,null=False,default='')
    park_image = models.TextField(default='') #reference external URL for Image
    park_contact = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.park_name


    class Meta:
        verbose_name = 'Park'
        verbose_name_plural = 'Park'

class ParkProperty(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    park_name = models.ForeignKey("Park", on_delete=models.CASCADE,related_name='prop.parkname+')
    property_name = models.CharField(max_length=255,blank=False,null=False,default='')
    property_description = models.TextField(default='')
    property_guest_capacity = models.IntegerField(null=True,blank=True)
    property_location = models.CharField(max_length=255,blank=True,null=True,default='')
    property_price = models.IntegerField(null=True,blank=True)
    property_image = models.TextField(default='') #reference external URL for Image
    property_slot = models.CharField(max_length=50,blank=True,null=True,default='2 hours')
    
    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name = 'ParkProperty'
        verbose_name_plural = 'ParkProperty'

class ParkPropertyAvailability(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    property_availability_date = models.DateField(auto_now=False, auto_now_add=False)
    property_availability_starttime = models.TimeField( auto_now=False, auto_now_add=False)
    property_availability_endtime = models.TimeField(auto_now=False, auto_now_add=False)
    property_name = models.ForeignKey("ParkProperty",on_delete=models.CASCADE,related_name='ava.propertyname+')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'ParkPropertyAvailability'
        verbose_name_plural = 'ParkPropertyAvailability'

class PropertyStatus(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    property_report_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    property_status_description = models.TextField(default='')
    property_expenses = models.IntegerField(null=True,blank=True)
    property_status_notes = models.TextField(default='')
    maint_staff_email = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    reservation_id = models.ForeignKey("Reservation",on_delete=models.CASCADE,related_name='status.resid+')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'PropertyStatus'
        verbose_name_plural = 'PropertyStatus'

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    res_slot = models.CharField(max_length=255,blank=True,null=True,default='')
    res_size = models.IntegerField(null=True,blank=True)
    res_status = models.CharField(max_length=255,blank=True,null=True,default='')
    renter_email = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    property_availability_id = models.ForeignKey("ParkPropertyAvailability", on_delete=models.CASCADE,related_name='res.propavailbilityid+')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservation'


class Transaction(models.Model):
    TRANS_TYPES = (('Credit Card','Credit Card'),('Android Pay','Android Pay'),('PayPal','PayPal'),('ApplePay','ApplePay'))
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,blank=False)
    transaction_amount = models.IntegerField(default='')
    transaction_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    transaction_type = models.CharField(choices=TRANS_TYPES,max_length=255,blank=True,null=True,default='')
    transaction_notes = models.TextField(default='')
    res_id = models.ForeignKey("Reservation", on_delete=models.CASCADE,related_name='trans.resid+')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transaction'

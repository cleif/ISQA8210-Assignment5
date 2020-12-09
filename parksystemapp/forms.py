from django import forms
from django.forms import ModelForm
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['res_size','res_slot','renter_email','property_availability_id']


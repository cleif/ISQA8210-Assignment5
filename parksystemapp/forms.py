from django import forms
from django.forms import ModelForm
from .models import Reservation

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ReservationForm(ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['res_eventdate','res_size','res_slot','renter_email','property_name']
        widgets = {
            'res_eventdate': DateTimeInput(),
        }
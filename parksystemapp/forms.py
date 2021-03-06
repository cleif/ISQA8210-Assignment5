from django import forms
from django.forms import ModelForm
from .models import Reservation, ParkPropertyAvailability, PropertyStatus

#for datetime
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

#for Date
class DateInput(forms.DateInput):
   input_type = 'date'

#for Time
class TimeInput(forms.TimeInput):
   input_type = 'time'

class ParkPropertyAvailabilityForm(ModelForm):
    class Meta:
        model = ParkPropertyAvailability
        fields = ['property_name', 'property_availability_date', 'property_availability_starttime', 'property_availability_endtime']
        widgets = {
            'property_availability_date': DateInput(),
            'property_availability_starttime': TimeInput(),
            'property_availability_endtime': TimeInput(),
        }

class PropertyStatusForm(ModelForm):
    class Meta:
        model = PropertyStatus
        fields = ['reservation_id','property_status_description','property_status_notes','property_expenses']


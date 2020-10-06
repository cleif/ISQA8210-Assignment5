from django.contrib import admin
from .models import Park, ParkProperty,ParkPropertyAvailbility,Reservation,PropertyStatus,Transaction
from users.models import CustomUser

class ParkAdmin(admin.ModelAdmin):
    model = Park
    list_display = ('id','park_name','park_addr','park_image')
    list_filter = ('id','park_name','park_addr','park_image')
    ordering = ['park_name']

class ParkPropertyAdmin(admin.ModelAdmin):
    model = ParkProperty
    list_display = ('id','park_name','property_name','property_description','property_guest_capacity','property_location','property_price','property_image','property_slot')
    list_filter = ('id','park_name','property_name','property_description','property_guest_capacity','property_location','property_price','property_image','property_slot')
    ordering = ['park_name']

class ParkPropertyAvailbilityAdmin(admin.ModelAdmin):
    model = ParkPropertyAvailbility
    list_display = ('id','property_name','property_availability_date','property_availability_starttime','property_availability_endtime')
    list_filter = ('id','property_name','property_availability_date','property_availability_starttime','property_availability_endtime')
    ordering = ['property_name']

class PropertyStatusAdmin(admin.ModelAdmin):
    model = PropertyStatus
    list_display = ('id','property_name','reservation_id','property_report_time','property_status_description','property_expenses','property_status_notes','maint_staff_email')
    list_filter = ('id','property_name','reservation_id','property_report_time','property_status_description','property_expenses','property_status_notes','maint_staff_email')
    ordering = ['property_name']

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('id','property_name','res_eventdate','res_slot','res_size','res_status','renter_email','property_availability_id')
    list_filter = ('id','property_name','res_eventdate','res_slot','res_size','res_status','renter_email','property_availability_id')
    ordering = ['property_name']

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('id','res_id','transaction_amount','transaction_date','transaction_type','transaction_notes')
    list_fileter = ('id','res_id','transaction_amount','transaction_date','transaction_type','transaction_notes')
    ordering = ['res_id']

admin.site.register(Park,ParkAdmin)
admin.site.register(ParkProperty,ParkPropertyAdmin)
admin.site.register(ParkPropertyAvailbility,ParkPropertyAvailbilityAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(PropertyStatus,PropertyStatusAdmin)
admin.site.register(Transaction,TransactionAdmin)


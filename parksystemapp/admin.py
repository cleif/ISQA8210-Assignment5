from django.contrib import admin
from .models import Park, ParkProperty,ParkPropertyAvailability,Reservation,PropertyStatus,Transaction
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

class ParkPropertyAvailabilityAdmin(admin.ModelAdmin):
    model = ParkPropertyAvailability
    list_display = ('id','get_parkname','property_name','property_availability_date','property_availability_starttime','property_availability_endtime')
    list_filter = ('id','property_name','property_availability_date','property_availability_starttime','property_availability_endtime')
    ordering = ['property_name']

    def get_parkname(self,obj):
        return obj.property_name.park_name.park_name
    get_parkname.short_description = 'Park'


class PropertyStatusAdmin(admin.ModelAdmin):
    model = PropertyStatus
    list_display = ('id','reservation_id','get_renteremail','property_report_time','property_status_description','property_expenses','property_status_notes','maint_staff_email')
    list_filter = ('id','reservation_id','property_report_time','property_status_description','property_expenses','property_status_notes','maint_staff_email')
    ordering = ['id']

    def get_renteremail(self,obj):
        return obj.reservation_id.renter_email
    get_renteremail.short_description = 'Renter Email'

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('id','get_parkname','get_propertyname','res_slot','res_size','res_status','renter_email','property_availability_id','get_resdate','get_resstart','get_resend')
    list_filter = ('id','res_slot','res_size','res_status','renter_email')
    ordering = ['id']

    def get_parkname(self,obj):
        return obj.property_availability_id.property_name.park_name.park_name
    get_parkname.short_description = 'park_name'

    def get_propertyname(self,obj):
        return obj.property_availability_id.property_name
    get_parkname.short_description = 'property_name'

    def get_resdate(self,obj):
        return obj.property_availability_id.property_availability_date
    get_resdate.short_description = 'res_date'

    def get_resstart(self,obj):
        return obj.property_availability_id.property_availability_starttime
    get_resstart.short_description = 'res_start'

    def get_resend(self,obj):
        return obj.property_availability_id.property_availability_endtime
    get_resend.short_description = 'res_end'


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('id','res_id','get_restransdate','get_restransstart','get_restransend','transaction_amount','transaction_date','transaction_type','transaction_notes')
    list_fileter = ('id','res_id','transaction_amount','transaction_date','transaction_type','transaction_notes')
    ordering = ['res_id']

    def get_restransdate(self,obj):
        return obj.res_id.property_availability_id.property_availability_date
    get_restransdate.short_description = 'Resveration Date'

    def get_restransstart(self,obj):
        return obj.res_id.property_availability_id.property_availability_starttime
    get_restransstart.short_description = 'Resveration Start'

    def get_restransend(self,obj):
        return obj.res_id.property_availability_id.property_availability_endtime
    get_restransend.short_description = 'Resveration End'

admin.site.register(Park, ParkAdmin)
admin.site.register(ParkProperty, ParkPropertyAdmin)
admin.site.register(ParkPropertyAvailability, ParkPropertyAvailabilityAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(PropertyStatus, PropertyStatusAdmin)
admin.site.register(Transaction, TransactionAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id','first_name','last_name','email','user_type','user_street_addr','user_city','user_state','user_zip','user_organization','user_phone','is_staff','is_superuser']


admin.site.register(CustomUser, CustomUserAdmin)

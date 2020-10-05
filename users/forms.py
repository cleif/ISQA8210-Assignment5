from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name','username','email','user_type','user_street_addr','user_city','user_state','user_zip','user_organization','user_phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','user_type','user_street_addr','user_city','user_state','user_zip','user_organization','user_phone')

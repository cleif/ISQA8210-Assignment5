from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import CustomUser
from django.views import generic, View
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name','email','user_street_addr','user_city','user_state','user_zip','user_organization','user_phone')
    template_name = 'user_edit.html'
    success_url = reverse_lazy('account')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('home')

def accountView(request):
    #user = request.user
    return render(request, 'account.html')

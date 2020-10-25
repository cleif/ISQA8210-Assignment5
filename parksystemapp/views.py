from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from .models import models
from .models import Park
from django.urls import reverse_lazy,reverse


class ParkListView(LoginRequiredMixin,ListView):
    model = Park
    template_name = 'park_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parks'] = Park.objects.all()
        return context

class ParkEditView(LoginRequiredMixin,UpdateView):
    model = Park
    fields = ('park_name', 'park_addr', 'park_image', 'park_contact')
    template_name = 'park_edit.html'

    def form_valid(self, form):
        form.instance.park = get_object_or_404(Park, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('park_list')

class ParkDeleteView(LoginRequiredMixin,DeleteView):
    model = Park
    template_name = 'park_delete.html'

    def get_success_url(self):
        return reverse('park_list')

class ParkCreateView(LoginRequiredMixin,CreateView):
    model = Park
    template_name = 'park_add.html'
    fields = ('park_name', 'park_addr', 'park_image', 'park_contact')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('park_list')
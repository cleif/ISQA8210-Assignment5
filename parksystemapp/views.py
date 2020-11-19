from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models, Park, ParkProperty, ParkPropertyAvailability,PropertyStatus,Reservation,Transaction
from django.urls import reverse_lazy,reverse
from PIL import Image


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

class ParkDetailView(LoginRequiredMixin,DetailView):
    model = Park
    template_name = 'park_detail.html'
    login_url = 'login'
    queryset = Park.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parkprops'] = ParkProperty.objects.all()
        return context

class ParkPropertyListView(LoginRequiredMixin,ListView):
    model = ParkProperty
    template_name = 'parkprop_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parkprops'] = ParkProperty.objects.all()
        return context


class ParkPropertyEditView(LoginRequiredMixin,UpdateView):
    model = ParkProperty
    fields = ('park_name', 'property_name', 'property_description', 'property_guest_capacity','property_location','property_price','property_image','property_slot')
    template_name = 'parkprop_edit.html'

    def form_valid(self, form):
        form.instance.parkprop = get_object_or_404(ParkProperty, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('parkprop_list')


class ParkPropertyDeleteView(LoginRequiredMixin,DeleteView):
    model = ParkProperty
    template_name = 'parkprop_delete.html'
    def get_success_url(self):
        return reverse('parkprop_list')


class ParkPropertyCreateView(LoginRequiredMixin,CreateView):
    model = ParkProperty
    template_name = 'parkprop_add.html'
    fields = ('park_name', 'property_name', 'property_description', 'property_guest_capacity','property_location','property_price','property_image','property_slot')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('parkprop_list')

class PropAvailabilityListView(LoginRequiredMixin,ListView):
    model = ParkPropertyAvailability
    template_name = 'propavailability_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['propavailability'] = ParkPropertyAvailability.objects.all()
        return context
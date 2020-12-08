from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView, TemplateView
from .models import models, Park, ParkProperty, ParkPropertyAvailability,PropertyStatus,Reservation,Transaction
from django.urls import reverse_lazy,reverse
from PIL import Image
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
import csv



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

class PropAvailabilityDetailView(LoginRequiredMixin,DetailView):
    model = ParkProperty
    template_name = 'propavailability_list.html'
    queryset = ParkProperty.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['propertyava'] = ParkPropertyAvailability.objects.all()
        return context

class PropReservationCreateView(LoginRequiredMixin,CreateView):
    model = Reservation
    template_name = 'reservation.html'
    fields = ['res_size','res_slot','property_availability_id','renter_email']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['propertyava'] = ParkPropertyAvailability.objects.all()
        return context
    
    def form_valid(self,form):
        form.instance.renter_email = self.request.user.username
        form.instance.propertyava = get_object_or_404(ParkPropertyAvailability, pk=self.kwargs['pk'])
        return super(PropReservationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('park_list')

    

class PropReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name  = 'reservation_detail.html'

class PropReservationDeleteView(LoginRequiredMixin,DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    def get_success_url(self):
        return reverse('parkprop_list')

class PropReservationListView(LoginRequiredMixin,ListView):
    model = Reservation
    template_name = 'reservation_list.html'




#....Reporting Exports...

class ReportTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'reporting.html'

def export_Park_toCSV(request):
    fields = [f.name for f in Park._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-Parks.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in Park.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response

def export_ParkProperty_toCSV(request):
    fields = [f.name for f in ParkProperty._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-ParkProperty.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in ParkProperty.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response

def export_ParkPropertyAvailability_toCSV(request):
    fields = [f.name for f in ParkPropertyAvailability._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-ParkPropertyAvailability.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in ParkPropertyAvailability.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response

def export_PropertyStatus_toCSV(request):
    fields = [f.name for f in PropertyStatus._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-PropertyStatus.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in PropertyStatus.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response

def export_Reservation_toCSV(request):
    fields = [f.name for f in Reservation._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-Reservation.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in Reservation.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response

def export_Transaction_toCSV(request):
    fields = [f.name for f in Transaction._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-Transaction.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in Transaction.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response
   

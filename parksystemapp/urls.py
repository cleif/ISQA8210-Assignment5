from django.urls import path
from . import views
from .views import (
    ParkListView,
    ParkEditView,
    ParkDeleteView,
    ParkCreateView,
    ParkDetailView,
    ParkPropertyListView,
    ParkPropertyEditView,
    ParkPropertyDeleteView,
    ParkPropertyCreateView,
    PropAvailabilityDetailView,
    PropReservationCreateView,
    PropReservationDetailView,
    PropReservationDeleteView,
    PropReservationListView,
    ReportTemplateView,
    UpdateDataTemplateView,
    PropAvailabilityCreateView, PropertyStatusEditView, PropertyStatusDeleteView, PropertyStatusCreateView,
    PropertyStatusListView,
)


urlpatterns = [

    path('park/<uuid:pk>/edit/', ParkEditView.as_view(), name='park_edit'),
    path('park/<uuid:pk>/delete/', ParkDeleteView.as_view(), name='park_delete'),
    path('parknew/', ParkCreateView.as_view(), name='park_add'),
    path('parklist/', ParkListView.as_view(), name='park_list'),
    path('<uuid:pk>/details', ParkDetailView.as_view(), name='park_details'),
    path('parkprop/<uuid:pk>/edit/',ParkPropertyEditView.as_view(), name='parkprop_edit'),
    path('parkprop/<uuid:pk>/delete/',ParkPropertyDeleteView.as_view(), name='parkprop_delete'),
    path('parkpropnew/', ParkPropertyCreateView.as_view(), name='parkprop_add'),
    path('parkproplist/', ParkPropertyListView.as_view(), name='parkprop_list'),
    path('parkprop/<uuid:pk>/propavailability', PropAvailabilityDetailView.as_view(), name='propavailability_list'),
    path('propavailability_create', PropAvailabilityCreateView.as_view(),name='propavailability_create'),
    path('parkprop/<uuid:pk>/reserve_create', PropReservationCreateView.as_view(), name='reservation'),
    path('parkprop/<uuid:pk>/reserve_detail', PropReservationDetailView.as_view(), name='reservation_detail'),
    path('parkprop/<uuid:pk>/cancel/',PropReservationDeleteView.as_view(), name='reservation_delete'),
    path('parkprop/<uuid:pk>/reservation_list/',PropReservationListView.as_view(), name='reservation_list'),
    path('propstatus/<uuid:pk>/edit/', PropertyStatusEditView.as_view(), name='propstatus_edit'),
    path('propstatus/<uuid:pk>/delete/', PropertyStatusDeleteView.as_view(), name='propstatus_delete'),
    path('propstatusnew/', PropertyStatusCreateView.as_view(), name='propstatus_add'),
    path('propstatuslist/', PropertyStatusListView.as_view(), name='propstatus_list'),

    #...Data Updates...
    path("UpdateData", UpdateDataTemplateView.as_view(), name="update_data"),
    #...Data Exports...
    path('reporting', ReportTemplateView.as_view(), name='reporting'),
    path('export_Park', views.export_Park_toCSV, name='export_Park'),
    path('export_ParkProperty', views.export_ParkProperty_toCSV, name='export_ParkProperty'),
    path('export_ParkPropertyAvailability', views.export_ParkPropertyAvailability_toCSV, name='export_ParkPropertyAvailability'),
    path('export_PropertyStatus', views.export_PropertyStatus_toCSV, name='export_PropertyStatus'),
    path('export_Reservation', views.export_Reservation_toCSV, name='export_Reservation'),
    path('export_Transaction', views.export_Transaction_toCSV, name='export_Transaction'),

    # Checkout 
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
    path('checkout/success/', views.SuccessView.as_view(), name='success')
]
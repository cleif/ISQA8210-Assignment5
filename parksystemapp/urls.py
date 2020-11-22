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
    path('parkprop/<uuid:pk>/reserve_create', PropReservationCreateView.as_view(), name='reservation'),
]
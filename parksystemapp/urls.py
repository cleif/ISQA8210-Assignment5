from django.urls import path
from . import views
from .views import (
    ParkListView,
    ParkEditView,
    ParkDeleteView,
    ParkCreateView,
    ParkPropertyListView,
    ParkPropertyEditView,
    ParkPropertyDeleteView,
    ParkPropertyCreateView,
)


urlpatterns = [

    path('park/<uuid:pk>/edit/', ParkEditView.as_view(), name='park_edit'),
    path('park/<uuid:pk>/delete/', ParkDeleteView.as_view(), name='park_delete'),
    path('parknew/', ParkCreateView.as_view(), name='park_add'),
    path('parklist/', ParkListView.as_view(), name='park_list'),
    path('parkprop/<uuid:pk>/edit/',ParkPropertyEditView.as_view(), name='parkprop_edit'),
    path('parkprop/<uuid:pk>/delete/',ParkPropertyDeleteView.as_view(), name='parkprop_delete'),
    path('parkpropnew/', ParkPropertyCreateView.as_view(), name='parkprop_add'),
    path('parkproplist/', ParkPropertyListView.as_view(), name='parkprop_list'),

]
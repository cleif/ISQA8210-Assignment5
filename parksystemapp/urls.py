from django.urls import path
from . import views
from .views import (
    ParkListView,
    ParkEditView,
    ParkDeleteView,
    ParkCreateView,
)


urlpatterns = [

    path('<uuid:pk>/edit/',ParkEditView.as_view(), name='park_edit'),
    path('<uuid:pk>/delete/',ParkDeleteView.as_view(), name='park_delete'),
    path('parknew/', ParkCreateView.as_view(), name='park_add'),
    path('parklist/', ParkListView.as_view(), name='park_list'),

]
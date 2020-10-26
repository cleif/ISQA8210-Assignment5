from django.urls import path
from .views import (
    SignUpView,
    UserUpdateView,
    UserDeleteView,
)
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<uuid:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('<uuid:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('account/', views.accountView, name='account'),
]

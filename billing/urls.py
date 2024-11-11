from django.urls import path
from .views import dashboard_bills

urlpatterns = [
    path('dashboard-bills', dashboard_bills, name='dashboard-bills'),
]
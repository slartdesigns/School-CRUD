from django.urls import path
from .views import dashboard_bills, bills, configuration_bills

urlpatterns = [
    path('dashboard-bills', dashboard_bills, name='dashboard-bills'),
    path('bills', bills, name='bills'),
    path('configuration-bills', configuration_bills, name='configuration-bills'),
]
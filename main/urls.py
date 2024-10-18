from django.urls import path
from .views import home, log_in, log_out, create_account

urlpatterns = [
    path('', home, name='home'),
    path('login', log_in, name='log_in'),
    path('logout', log_out, name='log_out'),
    path('create_account', create_account, name='create_account'),
]
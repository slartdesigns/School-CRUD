from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from dashboard.custom_models import emailBackend
from dashboard.views import dashboard_admins

# Create your views here.
def home(request):
    # return render(request, 'home.html')
    return redirect(dashboard_admins)


def create_account(request):
    if request.method == 'GET':
        return render(request, 'pages/create-account.html')
    else:
        if request.POST['password1'] == request.POST['password2'] and request.POST['policy_privacy'] == 'on':
            try:
                return HttpResponse('Email: ' + request.POST.get('email') + ' - Password: ' + request.POST['password1'] + ' - Policies: ' + request.POST['policy_privacy'])
            except:
                return render(request, 'pages/create-account.html', {
                    'error': 'El usuario ya existe',
                })
        else:
            return render(request, 'pages/create-account.html', {
                'error': 'Las contraseñas no coinciden',
            })


def log_in(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    else:
        user = emailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

        if user != None:
            login(request, user)
            return redirect(dashboard_admins)
        else:
            return HttpResponse('Login invalido')


def log_out(request):
    logout(request)
    return redirect(home)
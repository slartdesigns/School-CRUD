from django.shortcuts import redirect, render
from dashboard.models import CustomUser

# Create your views here.
s_user = CustomUser.objects.filter(user_type=3).all()

def auth_user(request) -> bool:
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return True
    else:
        return False

def dashboard_bills(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'dashboard_bills.html',{
                'suser': s_user,
            })
        else:
            pass
    else:
        return redirect('../login')
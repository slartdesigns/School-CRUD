from django.shortcuts import redirect, render
from dashboard.models import CustomUser, SchoolPeriod, Students
from .models import MonthlyCost, PaymentHistory

# Create your views here.
admin = CustomUser.objects.get(id=1)
s_user = CustomUser.objects.filter(user_type=3).all()
sch_p = SchoolPeriod.objects.all()
mon_c = MonthlyCost.objects.all()
pay_h = PaymentHistory.objects.all()

def auth_user(request) -> bool:
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return True
    else:
        return True

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
    

def bills(request):
    if auth_user(request) == True:
        monthly = mon_c.get(id=1)
        if request.method == 'GET':
            return render(request, 'bills.html',{
                'suser': s_user,
                'speriod': sch_p,
                'mcost': monthly,
                'payh': pay_h,
            })
        else:
            print(list(request.POST.items()))
            stu_id = Students.objects.get(admin_id=request.POST.get('student_id'))
            per_id = SchoolPeriod.objects.get(id=request.POST.get('school_period'))

            PaymentHistory.objects.create(
                amount_usd = request.POST.get('amount_usd'),
                amount_ves = request.POST.get('amount_ves'),
                daily_rate = 46.33,
                payment_type = request.POST.get('payment_type'),
                concept = request.POST.get('concept'),
                total = int(request.POST.get('amount_usd')) + int(request.POST.get('amount_ves')),
                processor_by = admin,
                student_id = stu_id,
                period_id = per_id,
            )

            print('Datos creados')
            return redirect('/auth/bills')
    else:
        return redirect('../login')
    

def configuration_bills(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'configuration_bills.html',{
                'mcost': mon_c,
                'speriod': sch_p,
            })
        else:
            # print(list(request.POST.items()))

            period = SchoolPeriod.objects.get(id=request.POST.get('school_period'))

            try:
                MonthlyCost.objects.create(
                    period_id = period,
                    month = request.POST.get('month'),
                    amount = request.POST.get('amount'),
                    expiry = request.POST.get('expiry')
                ).save()
                print('Datos creados')
                return redirect('/auth/configuration-bills')
            except:
                print('Fallo en la creacion de datos')
                return redirect('/auth/configuration-bills')
    else:
        return redirect('../login')
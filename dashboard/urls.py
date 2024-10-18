from django.urls import path
from .views import dashboard_admins, dashboard_bills, dashboard_teachers, dashboard_students, teachers, students, subjects, schedules, edit

urlpatterns = [
    path('dashboard-admins', dashboard_admins, name='dashboard-admins'),
    path('dashboard-bills', dashboard_bills, name='dashboard-bills'),
    path('dashboard-teachers', dashboard_teachers, name='dashboard-teachers'),
    path('dashboard-students', dashboard_students, name='dashboard-students'),
    path('teachers', teachers, name='teachers'),
    path('students', students, name='students'),
    path('subjects', subjects, name='subjects'),
    path('schedules', schedules, name='schedules'),
    path('edit', edit, name='edit'),
]

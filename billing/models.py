from django.db import models
from dashboard.models import CustomUser, Students, SchoolPeriod

# Create your models here.
class MonthlyCost(models.Model):
    id=models.AutoField(primary_key=True)
    month=models.CharField(max_length=50)
    amount=models.PositiveBigIntegerField(default=0)
    expiry=models.DateField()
    period_id=models.ForeignKey(SchoolPeriod,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    paid=models.PositiveIntegerField(default=0)
    debt=models.PositiveIntegerField(default=0)
    earring=models.PositiveIntegerField(default=0)
    discount=models.PositiveIntegerField(default=0)
    august=models.PositiveIntegerField(default=0)
    annuity=models.PositiveIntegerField(default=0)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    period_id=models.ForeignKey(SchoolPeriod,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class PaymentHistory(models.Model):
    id=models.AutoField(primary_key=True)
    amount_usd=models.PositiveIntegerField(default=0)
    amount_ves=models.PositiveIntegerField(default=0)
    daily_rate=models.PositiveIntegerField(default=0)
    payment_type_data=(
        (1,'Dolares (efectivo)'),
        (2,'Bolivares (efectivo)'),
        (3,'Transferencia'),
        (4,'Debito'),
        (5,'Pago movil'),
    )
    payment_type=models.CharField(choices=payment_type_data, max_length=50)
    concept_data=(
        (1,'Mensualidad'),
        (2,'Agosto'),
        (3,'Seguro escolar'),
        (4,'Comunidad educativa'),
        (5,'Gastos administrativos'),
        (6,'Conceptos varios'),
    )
    concept=models.CharField(choices=concept_data, max_length=50)
    details=models.CharField(max_length=255, blank=True)
    total=models.PositiveIntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    comment=models.CharField(max_length=255, blank=True)
    processor_by=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    period_id=models.ForeignKey(SchoolPeriod,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
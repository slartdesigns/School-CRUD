# Generated by Django 5.1.1 on 2024-11-11 05:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlycost',
            name='period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.schoolperiod'),
        ),
        migrations.AddField(
            model_name='payment',
            name='period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.schoolperiod'),
        ),
        migrations.AddField(
            model_name='payment',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.students'),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.schoolperiod'),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='processor_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.students'),
        ),
    ]

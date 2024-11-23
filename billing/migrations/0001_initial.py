# Generated by Django 5.1.1 on 2024-11-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=50)),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('expiry', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paid', models.PositiveIntegerField(default=0)),
                ('debt', models.PositiveIntegerField(default=0)),
                ('earring', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('august', models.PositiveIntegerField(default=0)),
                ('annuity', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount_usd', models.PositiveIntegerField(default=0)),
                ('amount_ves', models.PositiveIntegerField(default=0)),
                ('daily_rate', models.PositiveIntegerField(default=0)),
                ('payment_type', models.CharField(choices=[(1, 'Dolares (efectivo)'), (2, 'Bolivares (efectivo)'), (3, 'Transferencia'), (4, 'Debito'), (5, 'Pago movil')], max_length=50)),
                ('concept', models.CharField(choices=[(1, 'Mensualidad'), (2, 'Agosto'), (3, 'Seguro escolar'), (4, 'Comunidad educativa'), (5, 'Gastos administrativos'), (6, 'Conceptos varios')], max_length=50)),
                ('details', models.CharField(blank=True, max_length=255)),
                ('total', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

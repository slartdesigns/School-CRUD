# Generated by Django 5.1.1 on 2024-10-11 11:58

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(choices=[(1, 'Preescolar'), (2, 'Educ. Básica'), (3, 'Educ. Media')], max_length=20)),
                ('grade', models.CharField(choices=[(1, '1er nivel'), (2, '2do nivel'), (3, '3er nivel'), (4, '1er grado'), (5, '2do grado'), (6, '3er grado'), (7, '4to grado'), (8, '5to grado'), (9, '6to grado'), (10, '1er año'), (11, '2do año'), (12, '3er año'), (13, '4to año'), (14, '5to año')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guardians',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('idcard', models.PositiveIntegerField(default=0)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('profile_pic', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[(1, 'A'), (2, 'B')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'staff'), (3, 'users')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adminhod', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idcard', models.PositiveIntegerField(default=0)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('gender', models.CharField(choices=[(1, 'Masculino'), (2, 'Femenino'), (3, 'Otro')], max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.TextField()),
                ('profile_pic', models.FileField(upload_to='')),
                ('session_start', models.DateField(null=True)),
                ('session_end', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.courses')),
                ('guardian_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.guardians')),
                ('section_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.sections')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_type', models.CharField(choices=[(1, 'Planilla'), (2, 'Factura'), (3, 'Recibo'), (4, 'Diploma'), (5, 'Informe'), (6, 'Citación'), (7, 'Constancia')], max_length=30)),
                ('document', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.students')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ManyToManyField(to='dashboard.courses')),
                ('section_id', models.ManyToManyField(to='dashboard.sections')),
                ('subject_id', models.ManyToManyField(to='dashboard.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.courses')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sections')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subjects')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.teachers')),
            ],
        ),
    ]

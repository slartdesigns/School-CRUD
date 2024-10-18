from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    user_type_data=((1,'HOD'),(2,'staff'),(3,'users'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='adminhod')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    name_type_data = (
        (1,'Preescolar'),
        (2,'Educ. Básica'),
        (3,'Educ. Media')
        )
    name_type=models.CharField(choices=name_type_data, max_length=20,)
    grade_data = (
        (1,'1er nivel'),
        (2,'2do nivel'),
        (3,'3er nivel'),
        (4,'1er grado'),
        (5,'2do grado'),
        (6,'3er grado'),
        (7,'4to grado'),
        (8,'5to grado'),
        (9,'6to grado'),
        (10,'1er año'),
        (11,'2do año'),
        (12,'3er año'),
        (13,'4to año'),
        (14,'5to año')
        )
    grade=models.CharField(choices=grade_data,max_length=20,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Sections(models.Model):
    id=models.AutoField(primary_key=True)
    name_data=((1,'A'),(2,'B'))
    name=models.CharField(choices=name_data, max_length=10,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Teachers(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='teachers')
    phone=PhoneNumberField()
    address=models.TextField()
    course_id=models.ManyToManyField(Courses)
    subject_id=models.ManyToManyField(Subjects)
    section_id=models.ManyToManyField(Sections)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Guardians(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,)
    idcard=models.PositiveIntegerField(default=0)
    phone=PhoneNumberField()
    profile_pic=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='students')
    idcard=models.PositiveIntegerField(default=0)
    age=models.PositiveSmallIntegerField(default=0)
    gender_data=((1,'Masculino'),(2,'Femenino'),(3,'Otro'))
    gender=models.CharField(choices=gender_data, max_length=30)
    phone=PhoneNumberField()
    address=models.TextField()
    profile_pic=models.FileField()
    session_start=models.DateField(null=True)
    session_end=models.DateField(null=True)
    course_id=models.ForeignKey(Courses,on_delete=models.PROTECT, null=True)
    section_id=models.ForeignKey(Sections,on_delete=models.PROTECT, null=True)
    guardian_id=models.OneToOneField(Guardians,on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Documents(models.Model):
    id=models.AutoField(primary_key=True)
    doc_type_data = (
        (1,'Planilla'),
        (2,'Factura'),
        (3,'Recibo'),
        (4,'Diploma'),
        (5,'Informe'),
        (6,'Citación'),
        (7,'Constancia')
        )
    doc_type=models.CharField(choices=doc_type_data,max_length=30,)
    document=models.FileField()
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Schedules(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Sections,on_delete=models.CASCADE)
    start=models.TimeField()
    end=models.TimeField()
    day_data = (
        (1,'Lunes'),
        (2,'Martes'),
        (3,'Miércoles'),
        (4,'Jueves'),
        (5,'Viernes'),
        (6,'Sábado'),
        (7,'Domingo'),
        )
    day=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

# --------------------------------------------------------------
# ---- SIGNALS -------------------------------------------------
# --------------------------------------------------------------

# Receive a signal to create a new user with certain type
@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)

        if instance.user_type == 2:
            Teachers.objects.create(admin=instance)
            
        if instance.user_type == 3:
            Students.objects.create(admin=instance)

# Save the user
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()

    if instance.user_type == 2:
        instance.teachers.save()

    if instance.user_type == 3:
        instance.students.save()
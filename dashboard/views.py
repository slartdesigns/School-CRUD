from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Teachers, Students, Guardians, Subjects, Courses, Sections, Schedules, Tuition, SchoolPeriod

# Create your views here.
t_user = CustomUser.objects.filter(user_type=2).all()
s_user = CustomUser.objects.filter(user_type=3).all()
cou = Courses.objects.all()
sec = Sections.objects.all()
sub = Subjects.objects.all()
sch = Schedules.objects.all()
gua = Guardians.objects.all()
tui = Tuition.objects.all()
tea = Teachers.objects.all()

def auth_user(request) -> bool:
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return True
    else:
        return True


def dashboard_admins(request):
    if auth_user(request) == True:
        subj_list = [Subjects(name='Todas'),
                     Subjects(name='Matemáticas'),
                     Subjects(name='Biología'),
                     Subjects(name='Química'),
                     Subjects(name='Informática'),
                     Subjects(name='Robótica'),]
        
        sect_list = [Sections(name='A'),
                     Sections(name='B'),]
        
        cour_list = [Courses(name_type='Educ. Inicial', grade='1er nivel'),
                     Courses(name_type='Educ. Inicial', grade='2do nivel'),
                     Courses(name_type='Educ. Inicial', grade='3er nivel'),
                     Courses(name_type='Educ. Básica', grade='1er grado'),
                     Courses(name_type='Educ. Básica', grade='2do grado'),
                     Courses(name_type='Educ. Básica', grade='3er grado'),
                     Courses(name_type='Educ. Básica', grade='4to grado'),
                     Courses(name_type='Educ. Básica', grade='5to grado'),
                     Courses(name_type='Educ. Básica', grade='6to grado'),
                     Courses(name_type='Educ. Media', grade='1er año'),
                     Courses(name_type='Educ. Media', grade='2do año'),
                     Courses(name_type='Educ. Media', grade='3er año'),
                     Courses(name_type='Educ. Media', grade='4to año'),
                     Courses(name_type='Educ. Media', grade='5to año'),]
        if request.method == 'GET':
            s_count =  s_user.count()
            return render(request, 'dashboard_admins.html',{
                'scounts': s_count,
                'tuser': t_user,
                'suser': s_user,
            })
        else:
            try:
                Subjects.objects.bulk_create(subj_list)
                Sections.objects.bulk_create(sect_list)
                Courses.objects.bulk_create(cour_list)
                SchoolPeriod.objects.create(period='2024-2025').save()
                print('Datos creados')
                return redirect('/auth/dashboard-admins')
            except:
                print('Fallo en la creacion de datos')
                return redirect('/auth/dashboard-admins')
    else:
        return redirect('../login')


def dashboard_teachers(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'dashboard_teachers.html',{
                'schedules':sch,
            })
        else:
            pass
    else:
        return redirect('../login')


def dashboard_students(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'dashboard_students.html',{
                'schedules':sch,
            })
        else:
            pass
    else:
        return redirect('../login')


def teachers(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'teachers.html',{
                'tuser': t_user,
                'courses': cou,
                'sections': sec,
                'subjects': sub,
            })
        else:
            print(list(request.POST.items()))

            courses = request.POST.get('valueCourses')
            sections = request.POST.get('valueSections')
            subjects = request.POST.get('valueSubjects')
            address = request.POST.get('address')+', '+request.POST.get('municipality')+', '+request.POST.get('city')+', '+request.POST.get('state')+', '+request.POST.get('country')

            try:
                user = CustomUser.objects.create_user(
                    password='defaultPass',
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    user_type=2,
                )
                teacher = Teachers.objects.get(admin=user)
                teacher.type_idcard = request.POST.get('idtype')
                teacher.idcard = request.POST.get('idcard')
                teacher.gender = request.POST.get('gender')
                teacher.birthdate = request.POST.get('birthdate')
                teacher.phone = request.POST.get('phone')
                teacher.address = address
                teacher.status = request.POST.get('status')
                teacher.course_type = courses
                teacher.save()


                for section in sections:
                    if section != ',':
                        query = Sections.objects.get(id=section)
                        teacher.section_id.add(query)

                for subject in subjects:
                    if subject != ',':
                        query = Subjects.objects.get(id=subject)
                        teacher.subject_id.add(query)

                print('Profesor creado exitosamente')
                return redirect('/auth/teachers')
            except:
                print('Error en la creacion de profesor')
                return redirect('/auth/teachers')
    else:
        return redirect('../login')
    

def students(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'students.html',{
                'courses': cou,
                'sections': sec,
                'suser': s_user,
                'guardians': gua,
            })
        else:
            print(list(request.POST.items()))

            address = request.POST.get('address1')+', '+request.POST.get('municipality1')+', '+request.POST.get('city1')+', '+request.POST.get('state1')+', '+request.POST.get('country1')

            # try:
            user = CustomUser.objects.create_user(
                password='defaultPass',
                first_name=request.POST.get('first_name1'),
                last_name=request.POST.get('last_name1'),
                email=request.POST.get('email1'),
                user_type=3,
            )

            guardian_ins = Guardians.objects.create(
                name = request.POST.get('first_name2')+' '+request.POST.get('last_name2'),
                type_idcard = request.POST.get('idtype2'),
                idcard = request.POST.get('idcard2'),
                phone = request.POST.get('phone2'),
                email = request.POST.get('email2'),
                address = address,
                profile_pic = request.POST.get('profile_pic2'),
            )
            guardian_ins.save()

            tuition_ins = Tuition.objects.create(
                status = request.POST.get('status'),
                type_shooling = request.POST.get('shooling'),
                type_education = request.POST.get('education'),
                start_date = request.POST.get('startdate'),
            )
            tuition_ins.save()

            student = Students.objects.get(admin=user)
            student.type_idcard = request.POST.get('idtype1')
            student.idcard = request.POST.get('idcard1')
            student.gender = request.POST.get('gender')
            student.age = request.POST.get('age')
            student.birthdate = request.POST.get('birthdate')
            student.phone = request.POST.get('phone1')
            student.address = address
            student.profile_pic = request.POST.get('profile_pic1')
            student.course_id = cou.get(id=request.POST.get('course'))
            student.guardian_id = gua.get(id=guardian_ins.id)
            student.section_id = sec.get(id=request.POST.get('section'))
            student.tuition_id = tui.get(id=tuition_ins.id)
            student.save()

            print('Estudiante creado exitosamente')
            return redirect('/auth/students')
            # except:
            #     print('Error en la creacion de estudiante')
            #     return redirect('/auth/students')
    else:
        return redirect('../login')


def subjects(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'subjects.html',{
                'subjects': sub,
                'teachers': t_user,
                'schedules': sch,
            })
        else:
            try:
                subject = Subjects.objects.create(
                    name=request.POST.get('subject'),
                )
                subject.save()
                print('Materia creada correctamente')
                return redirect('/auth/subjects')
            except:
                print('Error en la creacion de materia')
                return redirect('/auth/subjects')
    else:
        return redirect('../login')


def schedules(request):
    if auth_user(request) == True:
        if request.method == 'GET':
            return render(request, 'schedules.html',{
                'courses': cou,
                'subjects': sub,
                'teachers': t_user,
                'sections': sec,
                'schedules': sch,
            })
        else:
            try:
                course = Courses.objects.get(id=request.POST.get('course'))
                subject = Subjects.objects.get(id=request.POST.get('subject'))
                section = Sections.objects.get(id=request.POST.get('section'))
                teacher = Teachers.objects.get(admin=request.POST.get('teacher'))

                schedule = Schedules.objects.create(
                    start = request.POST.get('start'),
                    end = request.POST.get('end'),
                    day = request.POST.get('day'),
                    course_id = course,
                    subject_id = subject,
                    section_id = section,
                    teacher_id = teacher,
                )
                schedule.save()

                # print(list(request.POST.items()))
                print('Horario creado con exito')
                return redirect('/auth/schedules')
            except:
                print('Error en la creacion del horario')
                return redirect('/auth/schedules')
    else:
        return redirect('../login')
    

def edit(request):
    print(request.POST.get('edit_btn'))
    return redirect('../')
    pass
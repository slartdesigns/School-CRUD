from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboard.models import CustomUser, Teachers, Students, Guardians, Subjects, Courses, Sections, Schedules

# Create your views here.
t_user = CustomUser.objects.filter(user_type=2).all()
s_user = CustomUser.objects.filter(user_type=3).all()
cou = Courses.objects.all()
sec = Sections.objects.all()
sub = Subjects.objects.all()
sch = Schedules.objects.all()
gua = Guardians.objects.all()
tea = Teachers.objects.all()

def auth_user(request) -> bool:
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return True
    else:
        return False


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
        
        cour_list = [Courses(name_type='Preescolar', grade='1er nivel'),
                     Courses(name_type='Preescolar', grade='2do nivel'),
                     Courses(name_type='Preescolar', grade='3er nivel'),
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
                print('Datos creados')
                return redirect('/auth/dashboard_admins')
            except:
                print('Fallo en la creacion de datos')
                return redirect('/auth/dashboard_admins')
    else:
        return redirect('../login')


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
            # print(list(request.POST.items()))

            courses = request.POST.get('valueCourses')
            sections = request.POST.get('valueSections')
            subjects = request.POST.get('valueSubjects')

            try:
                user = CustomUser.objects.create_user(
                    password='defaultPass',
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    user_type=2,
                )
                teacher = Teachers.objects.get(admin=user)
                teacher.address = request.POST.get('address')
                teacher.phone = request.POST.get('phone')
                teacher.save()

                for course in courses:
                    if course != ',':
                        query = Courses.objects.get(id=course)
                        teacher.course_id.add(query)

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
            try:
                user = CustomUser.objects.create_user(
                    password='defaultPass',
                    first_name=request.POST.get('first_name1'),
                    last_name=request.POST.get('last_name1'),
                    email=request.POST.get('email'),
                    user_type=3,
                )

                guardian_ins = Guardians.objects.create(
                    name = request.POST.get('first_name2')+' '+request.POST.get('last_name2'),
                    phone = request.POST.get('phone2'),
                    idcard = request.POST.get('idcard2'),
                    profile_pic = request.POST.get('profile_pic2'),
                )
                guardian_ins.save()

                student = Students.objects.get(admin=user)
                student.phone = request.POST.get('phone1')
                student.idcard = request.POST.get('idcard1')
                student.age = request.POST.get('age')
                student.gender = request.POST.get('gender')
                student.address = request.POST.get('address1')
                student.profile_pic = request.POST.get('profile_pic1')
                student.course_id = cou.get(id=request.POST.get('course'))
                student.guardian_id = gua.get(id=guardian_ins.id)
                student.section_id = sec.get(id=request.POST.get('section'))
                student.save()

                print('Estudiante creado exitosamente')
                return redirect('/auth/students')
            except:
                print('Error en la creacion de estudiante')
                return redirect('/auth/students')
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
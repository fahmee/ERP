from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm,DepartmentForm,StudentForm
from .models import Department,Student




def index(request):
    # if not request.user.is_authenticated():
        return render(request, 'collage/login.html')



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                departments =Department.objects.filter(user=request.user)
                return render(request, 'collage/index.html', {'departments': departments})
    context = {
        "form": form,
    }
    return render(request, 'collage/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                departments = Department.objects.filter(user=request.user)
                return render(request, 'collage/index.html', {'departments': departments})
            else:
                return render(request, 'collage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'collage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'collage/login.html')


def personal_detail(request):
    if request.method == "POST":
        departments = request.POST['Depart_name']
        sect_name = request.POST['sec_name']
        rollno = request.POST['roll_no']
        department= get_object_or_404(Department, Depart_name=departments,sec_name=sect_name)
        # user = authenticate(username=username, password=password)
        departments_student = department.student_set.all()
        for s in departments_student:
            print(s.roll_no,rollno)
            if str(s.roll_no) == rollno:
                student = s
                return render(request, 'collage/index_personal.html', {'student':student})
            else:
                return render(request, 'collage/personal_detail.html',{'error_message': 'student not found'})

    else:
        return render(request, 'collage/personal_detail.html')






def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'collage/login.html', context)


def create_department(request):
    if not request.user.is_authenticated:
        return render(request, 'collage/login.html')
    else:
        form = DepartmentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            department = form.save(commit=False)
            department.user = request.user
            # department.department_logo = request.FILES['department_logo']
            # file_type = department.department_logo.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'department': department,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'collage/create_class.html', context)
            department.save()
            return render(request, 'collage/detail.html', {'department': department})
        context = {
            "form": form,
        }
        return render(request, 'collage/create_department.html', context)


def create_student(request, department_id):
    form = StudentForm(request.POST or None, request.FILES or None)
    department= get_object_or_404(Department, pk=department_id)
    if form.is_valid():
        departments_student = department.student_set.all()
        for s in departments_student:
            if s.roll_no == form.cleaned_data.get("roll_no"):
                context = {
                    'department': department,
                    'form': form,
                    'error_message': 'You already added that student',
                }
                return render(request, 'collage/create_student.html', context)
        student = form.save(commit=False)
        student.department = department
       

        student.save()
        
        return render(request, 'collage/detail.html', {'department': department})
    context = {
        'department': department,
        'form': form,
    }
    return render(request, 'collage/create_student.html', context)









def detail(request, department_id):
    if not request.user.is_authenticated:
        return render(request, 'collage/login.html')
    else:
        user = request.user
        department = get_object_or_404(Department, pk=department_id)
        return render(request, 'collage/detail.html', {'department': department, 'user': user})



def delete_department(request, department_id):
    departments = Department.objects.get(pk=department_id)
    departments.delete()
    departments = Department.objects.filter(user=request.user)
    return render(request, 'collage/index.html', {'departments': departments})



def delete_student(request, department_id, student_id):
    department = get_object_or_404(Department, pk=department_id)
    student = Student.objects.get(pk=student_id)
    student.delete()
    return render(request, 'collage/detail.html', {'department': department})


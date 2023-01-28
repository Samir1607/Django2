from datetime import date
from django.shortcuts import render, HttpResponse
from .models import Employee
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'eApp/index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    print(context)
    return render(request, 'eApp/allEmp.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        phone = int(request.POST['phone'])
        # adding new obj
        # new_user = User(name = "samir Padekar" , city="Akole")
        # new_user.save()
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, role_id=role,
                           dept_id=dept, phone=phone, hire_date=date.today())
        new_emp.save()
        return HttpResponse('Employee Added Successfully....!!!')

    elif request.method == "GET":
        return render(request, 'eApp/addEmp.html')

    else:
        return HttpResponse('An Exception Error Has Been Occurred....!!!')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            samirp = Employee.objects.get(id=emp_id)
            samirp.delete()
            return HttpResponse('Employee has removed successfully....!!!')
        except:
            return HttpResponse("please return valid ID")


    emps = Employee.objects.all()
    context ={
        'emps': emps
    }
    return render(request, 'eApp//rmEmp.html', context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept :
            emps = emps.filter(dept__name__icontains = dept )
        if role :
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }

        return render(request,'eApp/allEmp.html', context)

    elif request.method == "GET":
        return render(request, 'eApp/filterEmp.html')
    else:
        return HttpResponse('Exception Has Been Occurred...!')
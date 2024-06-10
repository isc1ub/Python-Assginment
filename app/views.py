from django.shortcuts import render
from .models import Employee


# Create your views here.

def home(request):
    return render(request, 'home.html')


def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees.html', context)


def employee(request, id):
    employee = Employee.objects.get(pk=id)
    context = {'employee': employee}
    return render(request, 'employee.html', context)


def about(request):
    return render(request, 'about.html')

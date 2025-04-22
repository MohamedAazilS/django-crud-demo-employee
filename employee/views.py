from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    context = {
        "employees":employees
    }
    return render(request, "employee_list.html" , context)

def employee_form(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = Employee(
            emp_code = form.cleaned_data['emp_code'],
            fullname = form.cleaned_data['fullname'],
            mobile = form.cleaned_data['mobile'],
            position = form.cleaned_data['position']
            )
            employee.save()
            return HttpResponseRedirect("/employee")
    employee_list = Employee.objects.all()
    return render(request, "employee_form.html", {'form':form})

def employee_delete(request, id):
    employee = Employee.objects.get(id = id)
    employee.delete()
    return HttpResponseRedirect("/employee")

def employee_show(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee_show.html', {"employee":employee})

def employee_edit(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            employee.save()
            return HttpResponseRedirect("/employee")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'form':form})
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

def employee_delete(request):
    return

def employee_show(request, emp_code):
    employee = Employee.objects.get(emp_code=emp_code)
    print(employee.mobile)
    return render(request, 'employee_show.html', {"employee":employee})
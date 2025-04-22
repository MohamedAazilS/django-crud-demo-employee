from .views import employee_delete, employee_form, employee_list, employee_show
from django.urls import path
urlpatterns = [
    path("", employee_list, name= "employee_list"),
    path("new/", employee_form, name="employee_form"),
    path("<int:emp_code>", employee_show, name='employee_show')
]
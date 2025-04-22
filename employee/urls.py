from .views import employee_delete, employee_form, employee_list, employee_show, employee_edit
from django.urls import path
urlpatterns = [
    path("", employee_list, name= "employee_list"),
    path("new/", employee_form, name="employee_form"),
    path("<int:id>", employee_show, name='employee_show'),
    path("delete/<int:id>/", employee_delete, name='employee_delete'),
    path("update/<int:id>/", employee_edit, name="employee_edit"),
]
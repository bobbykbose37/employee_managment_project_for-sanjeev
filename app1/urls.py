from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('admin_template',views.admin_template,name="admin_template"),
    path('employee_registration',views.employee_registration,name="employee_registration"),
path('employee_search',views.employee_search,name="employee_search"),
path('employee_edit_view',views.employee_edit_view,name="employee_edit_view"),
path('employee_delete_view',views.employee_delete_view,name="employee_delete_view"),
    path('employee_registration_edit/<int:sid>',views.employee_registration_edit,name="employee_registration_edit"),
path('employee_registration_delete/<int:sid>',views.employee_registration_delete,name="employee_registration_delete"),
path('menu',views.menu,name="menu"),
   ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workers/', views.employees, name='employees'),
    path('batafsil/<int:id>/', views.employee, name='employee_detail'),
    path('haqida/', views.about, name='about'),
]

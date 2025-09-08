from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Staff


# Create your views here.
class StaffList(ListView):
    model = Staff
    ordering = 'labor_contract'
    template_name = 'employees.html'
    context_object_name = 'employees'


class StaffDetail(DetailView):
    model = Staff
    template_name = 'employee.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'id'

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Staff, Product
from .filters import StaffFilter
from .forms import StaffForm
from datetime import datetime, UTC


# Create your views here.
class StaffList(ListView):
    model = Staff
    ordering = 'labor_contract'
    template_name = 'employees.html'
    context_object_name = 'employees'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StaffFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now(UTC)
        context['potential_employee'] = None
        context['products'] = Product.objects.all()
        context['filterset'] = self.filterset
        return context


class StaffDetail(DetailView):
    model = Staff
    template_name = 'employee.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'id'


class StaffCreate(CreateView):
    form_class = StaffForm
    model = Staff
    template_name = 'employee_edit.html'


class StaffUpdate(UpdateView):
    form_class = StaffForm
    model = Staff
    template_name = 'employee_edit.html'
    pk_url_kwarg = 'id'


class StaffDelete(DeleteView):
    model = Staff
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('full_list')
    pk_url_kwarg = 'id'
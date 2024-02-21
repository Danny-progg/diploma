from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from main.forms import DoctorForm
from main.models import Doctors, Category


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'main/category_list.html', context)


class DoctorsListView(LoginRequiredMixin, ListView):
    model = Doctors
    extra_context = {
        'title': 'Врачи'
    }
    template_name = 'main/doctors_list.html'


class SpecificListView(LoginRequiredMixin, ListView):
    model = Doctors
    template_name = 'main/spec_doctors_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Категория: {category_item.name}'

        return context_data



class DoctorsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Doctors
    permission_required = 'main.create_doctor'
    form_class = DoctorForm
    success_url = reverse_lazy('main:service_list')

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class DoctorsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Doctors
    permission_required = 'main.change_doctor'
    form_class = DoctorForm
    success_url = reverse_lazy('main:service_list')

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class DoctorsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Doctors
    permission_required = 'main.delete_doctor'
    success_url = reverse_lazy('main:service_list')


class DoctorsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Doctors
    permission_required = 'main.detail_doctor'
    form_class = DoctorForm
    success_url = reverse_lazy('main:service_list')


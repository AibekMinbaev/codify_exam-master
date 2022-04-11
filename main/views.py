from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Worker


class WorkerListView(ListView):
    model = Worker
    context_object_name = 'worker_list'
    template_name = 'worker_list.html'
    

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['worker_list'] = Worker.objects.all()
        return context 

class WorkerCreateView(CreateView): # partically working
    model = Worker
    template_name = 'worker_form.html' # ?? 
    fields = ['name', 'birth_date', 'work_position', 'experience']


class WorkerDetailView(DetailView): # worker project 
    model = Worker
    template_name = 'worker_detail.html'


class WorkerDeleteView(DeleteView):  # isn't workiing  
    model = Worker
    template_name = 'worker_delete.html'  


class WorkerUpdateView(UpdateView): # isn't working 
    model = Worker
    template_name = 'worker_form.html'  




 

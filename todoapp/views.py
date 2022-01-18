from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import task

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = 'all_todos'
    model = task
    
class ToDoView(DetailView):
    template_name = "ToDo.html"
    model = task

class EditView(UpdateView):
    template_name = "edit.html"
    model = task
    
class CreateView(CreateView):
    template_name = "create.html"
    model = task
    fields = '__all__'
    
class DeleteView(DeleteView):
    template_name = "delete.html"
    model = task
    success_url = reverse_lazy("index")
    
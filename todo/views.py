from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo, List
from . import models
# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class List(ListView):
    model = Todo

class Detail(DetailView):
    model = Todo

class Create(CreateView):
    model = Todo
    
    # 編集対象にするフィールド
    fields = ["title", "description", "list", "scheduledTime"]

class Update(UpdateView):
    model = Todo

    fields = ["title", "description", "list", "scheduledTime"]

class Delete(DeleteView):
    model = Todo
    success_url = reverse_lazy("todolist")

class ListIndex(ListView):
    model = models.List

class CreateList(CreateView):
    model = models.List
    success_url = reverse_lazy("listindex")
    fields = ["name"]

class DeleteList(DeleteView):
    model = models.List
    success_url = reverse_lazy("listindex")
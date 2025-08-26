from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Subject
from .forms import SubjectForm
from django.http import HttpResponse

class SubjectListView(ListView):
    model = Subject
    template_name = "subjects/subject_list.html"

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "subjects/subject_confirm_delete.html"
    success_url = reverse_lazy('subject_list')

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo desde Django!")

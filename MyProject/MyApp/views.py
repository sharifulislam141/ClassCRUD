from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from MyApp import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.
class IndexView(ListView):
    context_object_name='musician_list'
    model = models.Musician

class AddMusician(CreateView):
    context_object_name='musician'
    model= models.Musician
    fields="__all__"
    
class UpdateMusician(UpdateView):
    model= models.Musician
    fields="__all__"

class DeleteMusician(DeleteView):
    model= models.Musician
    success_url=reverse_lazy('my_app:index')
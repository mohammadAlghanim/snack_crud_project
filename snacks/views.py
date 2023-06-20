from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snacks
from django.urls import reverse_lazy
# Create your views here.

class SnackPageView(ListView):
    template_name='snack_list.html'
    model = Snacks
    context_object_name = "snacks"

class DetailPageView(DetailView):
    template_name='snack_detail.html'
    model = Snacks

class CreateView(CreateView):
    template_name='snack_create.html'
    model=Snacks
    fields = ['name','description','purchaser']

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snacks
    fields = '__all__'
    success_url =reverse_lazy('snack_list')
class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snacks
    fields = '__all__'
    success_url =reverse_lazy('snack_list')


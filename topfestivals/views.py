from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = 'home.html'

class Festivals(TemplateView):
    template_name = 'Festivals.html'
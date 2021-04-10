from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = 'home.html'

def festival(request):
    if request.user.is_authenticated:
        return render(request, "festivals.html", {})
    else:
        return redirect('/accounts/login/')


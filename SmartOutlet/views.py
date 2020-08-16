from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
	return HttpResponse("Hello from the home page!")

def lights(request):
	my_dict = {'key': 'value'}
	return render(request, 'SmartOutlet/lights.html', context=my_dict)

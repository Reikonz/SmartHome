from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import RPi.GPIO as GPIO
import time

# Create your views here.
def index(request):
	my_dict = {'key': 'value'}
	return render(request, 'SmartOutlet/home.html', context=my_dict)

def outlets(request):
	my_dict = {'key': 'value'}
	return render(request, 'SmartOutlet/outlets.html', context=my_dict)

def toggle_outlet(request):
	if request.is_ajax:
		command = request.GET.get('command', None)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18,GPIO.OUT)
		if command == "on":			
			GPIO.output(18, True)
		else:
			GPIO.output(18, False)
			GPIO.cleanup()
	
	return JsonResponse({"error": "", "status": 200})

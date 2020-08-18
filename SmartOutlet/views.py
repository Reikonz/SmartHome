from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import RPi.GPIO as GPIO
import time

# Create your views here.
def index(request):
	return HttpResponse("Hello from the home page!")

def outlets(request):
	my_dict = {'key': 'value'}
	return render(request, 'SmartOutlet/outlets.html', context=my_dict)

def toggle_outlet(request):
	if request.is_ajax:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18,GPIO.OUT)
		GPIO.output(18, True)
		time.sleep(1)
		GPIO.output(18, False)
		time.sleep(1)
		GPIO.cleanup()
	return JsonResponse({"error": "", "status": 200})

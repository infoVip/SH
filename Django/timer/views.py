from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from timer.forms import TimerInfoForm
from timer.models import TimerInfo
import json

from django.core import serializers
  
# Create your views here.

def index(request):   
    return render(request, 'timer/index.html')

def add(request):  
    if request.method == 'POST':  
        form = TimerInfoForm(request.POST)  
        if form.is_valid():  
            timer_info = form.save()  
            timer_info.save()
            writein()
            return HttpResponse('OK')  
    else:  
        form = TimerInfoForm()

    return render(request, 'timer/add.html', {'form_info': form})  

def display(request):
    db = TimerInfo.objects.all()
    return render(request, 'timer/display.html', {'Timer': db})


def dispjson(request):
    data = serializers.serialize("json", TimerInfo.objects.all())
    return render(request, 'timer/dispjson.html', {'dt': data})


def writein():
    data = serializers.serialize("json", TimerInfo.objects.all())
    data = json.loads(data)
    
    for i in ['week0','week1','week2','week3','week4','week5','week6','week7']:
        pj = data[-1]['fields'][i]
        if pj:
            f = file( i,'a')
            for j in ['starttime','endtime','command1','command2']:
                temp = str(data[-1]['fields'][j])
                f.write(j)
                f.write('|')
                f.write(temp)
                f.write('|')
            f.write('\r\n')
            f.close()

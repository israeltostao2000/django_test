from django.shortcuts import render
from django.http import JsonResponse
from .forms import ledForm
from .models import Led, LedResult
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json
# Create your views here.
def home(request):
    responde = {
        "message": "Hey there",
    }
    return JsonResponse(responde)

def get_last_primary_key(request):
    try:
        last_entry = Led.objects.latest('id')
        last_pk = last_entry.id
    except Led.DoesNotExist:
        last_pk = None

    return JsonResponse({'last_pk': last_pk})

@csrf_exempt


def show_led_result(request, led_id):
    
    if request.method=="POST":

        data = json.loads(request.body)
        key = data.get('key')
        times_on = data.get('times_on')
        times_off = data.get('times_off')
        number_cycle = data.get('number_cycle')
        simulation_time = data.get('simulation_time')

        # Create and save the model instance
        led_result = LedResult(key=key, times_on=times_on, times_off=times_off, number_cycle=number_cycle, simulation_time=simulation_time)
        led_result.save()
        return JsonResponse(data)
    if request.method== "GET":
        led_show = LedResult.objects.get(key=led_id)
        data1 = {
                'key': led_show.key,
                'times_on': led_show.times_on,
                'times_off': led_show.times_off,
                'number_cycle': led_show.number_cycle,
                'simulation_time': led_show.simulation_time
        }

        return JsonResponse(data1)


def show_led(request, led_id):
    led_show = Led.objects.get(pk=led_id)
    data = {
                'key': led_show.key,
                'title': led_show.title,
                'time_on': led_show.time_on,
                'time_off': led_show.time_off,
                'simulation_time': led_show.simulation_time
    }
    
    if request.method=="GET":
        return JsonResponse(data)

def led_form(request):
    submitted = False
    if request.method == "POST":
        form = ledForm(request.POST)
        if form.is_valid():
            
            form.save()
            # pk1 = pk.pk
            # data = {
            #     'title': pk.title,
            #     'time_on': pk.time_on,
            #     'time_off': pk.time_off,
            #     'simulation_time': pk.simulation_time,
            # }
            

            #return HttpResponseRedirect('/led')
            
            #return JsonResponse(data)
           
            # Handle the case where the request failed
                
    else:
        form = ledForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'led/led.html', {'form': form, 'submitted': submitted})

"""Platzi views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse #usado en numeros_1

#Utilities
from datetime import datetime
import json #usado en numeros_2

def hello_world(request):
    return HttpResponse('Hello world!, current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def numeros_1(request):
    #import pdb; pdb.set_trace() #inicia un debuger
    numbers = request.GET['numbers']
    numbers = [int(i) for i in numbers.split(',')]
    numbers = sorted(numbers)
    data = {
        'satatus': 'ok',
        'ordered_numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    return JsonResponse(data) #asi se responde con el JsonResponse


def numeros_2(request):
    #import pdb; pdb.set_trace() #inicia un debuger
    numbers = request.GET['numbers']
    numbers = [int(i) for i in numbers.split(',')]
    numbers = sorted(numbers)
    data = {
        'satatus': 'ok',
        'ordered_numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'. format(name)
    else:
        message = 'Hello! {}, welcome to Platzi!'. format(name)

    return HttpResponse(message)

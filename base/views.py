from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    users = [
        {
            'name': 'Leandro',
            'sign': 'sagitarius',
            'age': 20,
            'height': 1.87
        },
        {
            'name': 'Lucy',
            'sign': 'aries',
            'age': 21,
            'height': 1.64
        }
    ]
    return render(request, 'hello.html', context={'users': users})

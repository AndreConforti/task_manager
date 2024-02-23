from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse(f'{email} | {password}')


def register(request):
    return render(request, 'register.html')
from django.shortcuts import render

def home(request):
    return render(request, 'APP/home.html')

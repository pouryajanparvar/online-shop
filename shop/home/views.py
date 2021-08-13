from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


def Home(request):
    return render(request, 'home/homepage.html', {})
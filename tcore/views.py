from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    
    deneme = model.objects.all()
    akor = accordion.objects.all()
    context={
        'deneme':deneme,
        'akor':akor
    }
    
    
    return render(request, 'index.html', context)
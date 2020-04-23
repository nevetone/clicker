from django.shortcuts import render
from database.models import Units, Islands, Mobs

# Create your views here.

def home(request):
    template="index.html"
    try:
        units = Units.objects.all()
        islands = Islands.objects.all()
        mobs = Mobs.objects.all()
    except:
        units = None
        islands = None
        mobs = None
        
    context={
        'units':units, 'islands':islands, 'mobs':mobs,
    }
    return render(request, template, context)
    

def test(request):
    template="test.html"
    try:
        units = Units.objects.all()
        islands = Islands.objects.all()
        mobs = Mobs.objects.all()
    except:
        units = None
        islands = None
        mobs = None
        
    context={
        'units':units, 'islands':islands, 'mobs':mobs,
    }
    return render(request, template, context)
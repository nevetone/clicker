from django.shortcuts import render
from database.models import Units, Islands, Mobs, Skills
import json
from .forms import Cookies
from django.shortcuts import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.

def home(request):
    template="index.html"
    try:
        units = Units.objects.all()
        islands = Islands.objects.all()
        mobs = Mobs.objects.all()
        skills = Skills.objects.all()
    except:
        units = None
        islands = None
        mobs = None
        skills = None

    if request.method == 'POST':
        cookie = request.POST.get('cookie_id')
        first_login = request.POST.get('first_login')
        message = 'Auto Save Complited'
        return HttpResponse(json.dumps({'message':message}), content_type="application/json")
    else:
        message = None
    
    context={
        'units':units, 'islands':islands, 'mobs':mobs, 'skills':skills,
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
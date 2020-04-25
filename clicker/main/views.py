from django.shortcuts import render
from database.models import Units, Islands, Mobs, Skills
import json
from .forms import Cookies
from django.shortcuts import Http404, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.http import JsonResponse
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
        current_gold = request.POST.get('current_gold')
        click_count = request.POST.get('click_count')
        stage = request.POST.get('stage')
        stage_passed =  request.POST.get('stage_passed')
        click_upgrades_bought = request.POST.get('click_upgrades_bought')
        var_o =  request.POST.get('var_o')
        clickUpgradePrice = request.POST.get('clickUpgradePrice')
        
        try:
            userid, created = Cookies.objects.get_or_create(cookies_id = cookie)
            if created:
                userid.current_gold = 99999999
                userid.click_count = 0
                userid.stage = 1
                userid.stage_passed = 1
                userid.click_upgrades_bought = 1
                userid.var_o = -1
                userid.clickUpgradePrice = 100
                userid.save()
                print(str(userid)+' :stworzony nowy')
            
            userid.current_gold = float(current_gold)
            userid.click_count = float(click_count)
            userid.stage = float(stage)
            userid.stage_passed = float(stage_passed)
            userid.click_upgrades_bought = float(click_upgrades_bought)
            userid.var_o = float(var_o)
            userid.clickUpgradePrice = float(clickUpgradePrice)
            userid.save()
            print(str(userid)+' :save udane')
        except:
            pass
        

        message = 'Auto Save Complited'
        return HttpResponse(json.dumps({'message':message}), content_type="application/json")
    else:
        message = None
        userid = None
    
    

    
    
    
    context={
        'units':units, 'islands':islands, 'mobs':mobs, 'skills':skills, 'userid':userid,
    }
    return render(request, template, context)








def load(request):
    if request.method == 'POST':
        userCookie = request.POST.get('loadUser')
        
        try:
            userCookies = Cookies.objects.get(cookies_id = userCookie)
        except:
            userCookies = None
            pass
        
        return JsonResponse({
            'var_o': userCookies.var_o,
            'click_count': userCookies.click_count,
            'stage': userCookies.stage,
            'stage_passed': userCookies.stage_passed,
            'current_gold': userCookies.current_gold,
            'click_upgrades_bought': userCookies.click_upgrades_bought,
            'clickUpgradePrice':userCookies.clickUpgradePrice,
            }, status=200)
    else:
        userCookies = None
        
    context={}
    template="index.html"
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
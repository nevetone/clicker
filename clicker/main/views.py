from django.shortcuts import render
from database.models import Units, Islands, Mobs, Skills
import json
from .models import Cookies, UserUnits
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
    
    try:
        unitsCount = Units.objects.all()
        unitsCount2 = Units.objects.all().count()
    except:
        pass
        
        # save
    if request.method == 'POST':
        cookie = request.POST.get('cookie_id')
        current_gold = request.POST.get('current_gold')
        click_count = request.POST.get('click_count')
        stage = request.POST.get('stage')
        stage_passed =  request.POST.get('stage_passed')
        click_upgrades_bought = request.POST.get('click_upgrades_bought')
        var_o =  request.POST.get('var_o')
        clickUpgradePrice = request.POST.get('clickUpgradePrice')
        price = []
        count = []
        name = []
        pomocnicza = 0

        try:
            get_user = Cookies.objects.get(cookies_id = cookie)
            
        except:
            pass
        
        try:
            user_units = UserUnits.objects.filter(cookies_id = get_user)
            user_units_count = UserUnits.objects.filter(cookies_id = get_user).count()
        except:
            user_units = None
            user_units_count = 0
        
        ile = 0
        if user_units_count < unitsCount2:
            try:
                user_units.delete()
                for unit in unitsCount:
                    k = UserUnits(cookies_id = get_user, unit_type=unit.unit_name, unit_cost=unit.unit_default_cost, unit_count=unit.unit_count)
                    k.save()
                    ile = ile + 1
                print('stworzono units x'+str(ile))
            except:
                pass

        
        
        if user_units is not None:
            for t in user_units:
                price.append(request.POST.get('price'+str(pomocnicza)))
                count.append(request.POST.get('count'+str(pomocnicza)))
                name.append(request.POST.get('name'+str(pomocnicza)))
                t.unit_type = str(name[pomocnicza])
                t.unit_cost = float(price[pomocnicza])
                t.unit_count = float(count[pomocnicza])
                t.save()
                pomocnicza = pomocnicza + 1

        name = []
        price = []
        count = []
        
        
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
            unitsCount = Units.objects.all()
        except:
            userCookies = None
            unitsCount = None
            pass
        
        try:
            user_units_count = UserUnits.objects.filter(cookies_id = userCookies).count()
            user_units = UserUnits.objects.filter(cookies_id = userCookies)
        except:
            pass
        
        
        try:
            print('Wczytywanie')
            context = {
                'var_o': userCookies.var_o,
                'click_count': userCookies.click_count,
                'stage': userCookies.stage,
                'stage_passed': userCookies.stage_passed,
                'current_gold': userCookies.current_gold,
                'click_upgrades_bought': userCookies.click_upgrades_bought,
                'clickUpgradePrice':userCookies.clickUpgradePrice,
                }
            
            pomocnicza = 0
            
            unit_cost = []
            unit_count = []
            
            for unit in user_units:
                unit_cost.append(unit.unit_cost)
                unit_count.append(unit.unit_count)
                
                context['unit_cost'] = unit_cost
                context['unit_count'] = unit_count
                pomocnicza = pomocnicza + 1
                
            unit_cost = []
            unit_count = []
            return JsonResponse(context, status=200)
        except:
            print('nie ma takiego usera')

            context2 = {
                'var_o': -1,
                'click_count': 0,
                'stage': 1,
                'stage_passed': 1,
                'current_gold': 998999,
                'click_upgrades_bought': 1,
                'clickUpgradePrice':100,
                }
            pomocnicza2 = 0
            for units in unitsCount:
                unit_cost.append(units.unit_cost)
                unit_count.append(units.unit_count)
                pomocnicza2 = pomocnicza2 + 1
                context2['unit_cost'] = unit_cost
                context2['unit_count'] = unit_count
            unit_cost = []
            unit_count = []
            return JsonResponse(context2, status=200)
            
        
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
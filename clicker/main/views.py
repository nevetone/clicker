from django.shortcuts import render
from database.models import Units, Islands, Mobs, Skills
import json
from .models import Cookies, UserUnits, UserSkills
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
    try:
        skillsCount = Skills.objects.all()
        skillsCount2 = Skills.objects.all().count()
    except:
        pass
        
        # save
    if request.method == 'POST':
        cookie = request.POST.get('cookie_id')
        visibleUpgrades = request.POST.get('visibleUpgrades')
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
        skill_price = []
        skill_count = []
        skill_name = []
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
        # units
        if user_units_count < unitsCount2:
            try:
                user_units.delete()
                for unit in unitsCount:
                    k = UserUnits(cookies_id = get_user, unit_type=unit.unit_name, unit_cost=unit.unit_default_cost, unit_count=unit.unit_count)
                    k.save()
            except:
                pass
        try:
            user_skills = UserSkills.objects.filter(cookies_id = get_user)
            user_skills_count = UserSkills.objects.filter(cookies_id = get_user).count()
        except:
            user_skills = None
            user_skills_count = 0
        # skills
        if user_skills_count < skillsCount2:
            try:
                user_skills.delete()
                for skill in skillsCount:
                    g = UserSkills(cookies_id = get_user, skill_type=skill.skill_name, skill_cost=skill.skill_cost, skill_count=skill.skill_count)
                    g.save()
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
        pomocnicza = 0
        
        
        if user_skills is not None:
            for i in user_skills:
                skill_price.append(request.POST.get('skill_price'+str(pomocnicza)))
                skill_count.append(request.POST.get('skill_count'+str(pomocnicza)))
                skill_name.append(request.POST.get('skill_name'+str(pomocnicza)))
                i.skill_type = str(skill_name[pomocnicza])
                i.skill_cost = float(skill_price[pomocnicza])
                i.skill_count = float(skill_count[pomocnicza])
                i.save()
                pomocnicza = pomocnicza + 1
        
        
        skill_price = []
        skill_count = []
        skill_name = []
        pomocnicza = 0
        
        try:
            userid, created = Cookies.objects.get_or_create(cookies_id = cookie)
            if created:
                userid.visibleUpgrades = -1
                userid.current_gold = 99999999
                userid.click_count = 0
                userid.stage = 1
                userid.stage_passed = 1
                userid.click_upgrades_bought = 1
                userid.var_o = -1
                userid.clickUpgradePrice = 100
                userid.save()
                
            userid.visibleUpgrades = float(visibleUpgrades)
            userid.current_gold = float(current_gold)
            userid.click_count = float(click_count)
            userid.stage = float(stage)
            userid.stage_passed = float(stage_passed)
            userid.click_upgrades_bought = float(click_upgrades_bought)
            userid.var_o = float(var_o)
            userid.clickUpgradePrice = float(clickUpgradePrice)
            userid.save()


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
            skillsCount = Skills.objects.all()
        except:
            userCookies = None
            unitsCount = None
            skillsCount = None
            pass
        
        try:
            user_units = UserUnits.objects.filter(cookies_id = userCookies)
            user_skills = UserSkills.objects.filter(cookies_id = userCookies)
        except:
            pass
        
        
        unit_cost = []
        unit_count = []
        skill_price = []
        skill_count = []
        
        
        try:
            print('Wczytywanie')
            context = {
                'visibleUpgrades' : userCookies.visibleUpgrades,
                'var_o': userCookies.var_o,
                'click_count': userCookies.click_count,
                'stage': userCookies.stage,
                'stage_passed': userCookies.stage_passed,
                'current_gold': userCookies.current_gold,
                'click_upgrades_bought': userCookies.click_upgrades_bought,
                'clickUpgradePrice':userCookies.clickUpgradePrice,
                }
            
            
            for unit in user_units:
                unit_cost.append(unit.unit_cost)
                unit_count.append(unit.unit_count)
                
                context['unit_cost'] = unit_cost
                context['unit_count'] = unit_count
                
            
            for skill in user_skills:
                skill_price.append(skill.skill_cost)
                skill_count.append(skill.skill_count)
                
                context['skill_price'] = skill_price
                context['skill_count'] = skill_count
            
            
            skill_price = []
            skill_count = []
            unit_cost = []
            unit_count = []
            return JsonResponse(context, status=200)
        except:
            context2 = {
                'visibleUpgrades' : -1,
                'var_o': -1,
                'click_count': 0,
                'stage': 1,
                'stage_passed': 1,
                'current_gold': 998999,
                'click_upgrades_bought': 1,
                'clickUpgradePrice':100,
                }

            for units in unitsCount:
                unit_cost.append(units.unit_default_cost)
                unit_count.append(units.unit_count)
                
                context2['unit_cost'] = unit_cost
                context2['unit_count'] = unit_count
                
                
            
            for skills in skillsCount:
                skill_price.append(skills.skill_cost)
                skill_count.append(skills.skill_count)
                
                context2['skill_price'] = skill_price
                context2['skill_count'] = skill_count
            
            
            skill_price = []
            skill_count = []
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
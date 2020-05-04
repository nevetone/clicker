from django.shortcuts import render
from database.models import Units, Islands, Mobs, Skills
import json
from .models import Cookies, UserUnits, UserSkills, UserPassives
from django.shortcuts import Http404, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.http import JsonResponse
# Create your views here.


def home(request):
    template="index.html"
    try:
        units = Units.objects.all()
    except:
        units = None
    try:
        islands = Islands.objects.all()
    except:
        islands = None
    try:
        mobs = Mobs.objects.all()
    except:
        mobs = None
    try:
        skills = Skills.objects.all()
    except:
        skills = None
        
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
        current_passive_points = request.POST.get('current_passive_points')
        current_mana = request.POST.get('current_mana')
        max_mana = request.POST.get('max_mana')
        price = []
        count = []
        name = []
        skill_price = []
        skill_count = []
        skill_name = []
        passive_id = []
        passive_cost = []
        passive_count = []
        pomocnicza = 0
        
        try:
            cookie_user =  Cookies.objects.get(cookies_id = cookie)
        except:
            cookie_user = None
        try:
            user_units = UserUnits.objects.filter(cookies_id = cookie_user)
            if not user_units:
                user_units = None
        except:
            user_units = None
        try:
            user_passives = UserPassives.objects.filter(cookies_id = cookie_user)
            if not user_passives:
                user_passives = None
        except:
            user_passives = None
            
        try:
            user_skills = UserSkills.objects.filter(cookies_id = cookie_user)
            if not user_skills:
                user_skills = None
        except:
            user_skills = None
        
        
        if cookie_user is None:
            try:
                cookie_user = Cookies(cookies_id = cookie, current_gold = 999999, click_count=0, stage=1, stage_passed=1, click_upgrades_bought=1, var_o=-1, clickUpgradePrice=100, visibleUpgrades=-1, current_passive_points=0, current_mana=100, max_mana=100 )
                cookie_user.save()
                print('tworzenie usera przy save')
            except:
                pass
            try:
                cookie_user =  Cookies.objects.get(cookies_id = cookie)
                print('sprawdzanie usera przy save')
            except:
                cookie_user = None
                message = "cannot find user" 
                return JsonResponse({'message':message, 'saved':'false'}, status=200)
        if user_units is None:
            for unit in units:
                user_units = UserUnits(cookies_id=cookie_user, unit_type = unit.unit_name, unit_cost = unit.unit_default_cost, unit_count = unit.unit_count)
                user_units.save()
            print('tworzenie units przy save')
            try:
                user_units = UserUnits.objects.filter(cookies_id = cookie_user)
            except:
                user_units = None
                message = "cannot find user units" 
                return JsonResponse({'message':message, 'saved':'false'}, status=200)
        if user_skills is None:
            for skill in skills:
                user_skills = UserSkills(cookies_id=cookie_user, skill_type = skill.skill_name, skill_cost = skill.skill_cost, skill_count = skill.skill_count)
                user_skills.save()
            print('tworzenie skills przy save')
            try:
                user_skills = UserSkills.objects.filter(cookies_id = cookie_user)
            except:
                user_skills = None
                message = "cannot find user skills" 
                return JsonResponse({'message':message, 'saved':'false'}, status=200)
        if user_passives is None:
            for x in range(0,10):
                user_passives = UserPassives(cookies_id = cookie_user, passive_id="passive"+str(x), passive_count = 0, passive_cost = 0)
                user_passives.save()
            print('tworzenie passives przy save')
            try:
                user_passives = UserPassives.objects.filter(cookies_id = cookie_user)
            except:
                user_passives = None
                message = "cannot find user passives" 
                return JsonResponse({'message':message, 'saved':'false'}, status=200)
        if user_units is not None and user_skills is not None and cookie_user is not None:
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
                print("Zapisano units")
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
                print("Zapisano skills")
            skill_price = []
            skill_count = []
            skill_name = []
            pomocnicza = 0
            
            if user_passives is not None:
                for x in user_passives:
                    passive_id.append(request.POST.get("passives"+str(pomocnicza)))
                    passive_cost.append(request.POST.get("passives"+str(pomocnicza)+"_cost"))
                    passive_count.append(request.POST.get("passives"+str(pomocnicza)+"_count"))
                    x.passive_id = str(passive_id[pomocnicza])
                    x.passive_count = float(passive_count[pomocnicza])
                    x.passive_cost = float(passive_cost[pomocnicza])
                    x.save()
                    pomocnicza = pomocnicza + 1
                print("Zapisano passives")
            passive_id = []
            passive_cost = []
            passive_count = []
            pomocnicza = 0
                
            cookie_user = Cookies.objects.get(cookies_id = cookie)
            cookie_user.visibleUpgrades = float(visibleUpgrades)
            cookie_user.current_gold = float(current_gold)
            cookie_user.click_count = float(click_count)
            cookie_user.stage = float(stage)
            cookie_user.max_mana = float(max_mana)
            cookie_user.stage_passed = float(stage_passed)
            cookie_user.click_upgrades_bought = float(click_upgrades_bought)
            cookie_user.var_o = float(var_o)
            cookie_user.current_mana = float(current_mana)
            cookie_user.current_passive_points = float(current_passive_points)
            cookie_user.clickUpgradePrice = float(clickUpgradePrice)
            cookie_user.save()
            message = 'Auto Save Complited'
            print('Zapisano Usera')
            return JsonResponse({'message':message, 'saved':'true'}, status=200)
        else:
            message = "cannot save - error" 
            return JsonResponse({'message':message, 'saved':'false'}, status=200)
    
    cookie_user = None
    context={'units':units, 'islands':islands, 'mobs':mobs, 'skills':skills, 'userid':cookie_user,}
    return render(request, template, context)

def load(request):
    try:
        if request.method == 'POST':
            userCookie = request.POST.get('loadUser')
            firstLogIn = request.POST.get('firstLogin1')
            print(firstLogIn)
            try:
                userCookies = Cookies.objects.get(cookies_id = userCookie)
            except:
                userCookies = None
            try:
                unitsCount = Units.objects.all()
            except:
                unitsCount = None
            try:
                skillsCount = Skills.objects.all()
            except:
                skillsCount = None
            try:
                user_units = UserUnits.objects.filter(cookies_id = userCookies)
                if not user_units:
                    user_units = None
                user_skills = UserSkills.objects.filter(cookies_id = userCookies)
                if not user_skills:
                    user_skills = None
            except:
                pass
            try:
                user_passives = UserPassives.objects.filter(cookies_id = userCookies)
                if not user_passives:
                    user_passives = None
            except:
                user_passives = None
            unit_cost = []
            unit_count = []
            skill_price = []
            skill_count = []
            passive_cost = []
            passive_count = []
            if firstLogIn == "False":
                print('Wczytywanie')
                context = {
                    'visibleUpgrades' : userCookies.visibleUpgrades,
                    'var_o': userCookies.var_o,
                    'click_count': userCookies.click_count,
                    'stage': userCookies.stage,
                    'stage_passed': userCookies.stage_passed,
                    'current_gold': userCookies.current_gold,
                    'click_upgrades_bought': userCookies.click_upgrades_bought,
                    'clickUpgradePrice': userCookies.clickUpgradePrice,
                    'current_passive_points': userCookies.current_passive_points,
                    'current_mana': userCookies.current_mana,
                    'max_mana': userCookies.max_mana,
                    }
                print("Wczytanie Usera")
                for unit in user_units:
                    unit_cost.append(unit.unit_cost)
                    unit_count.append(unit.unit_count)
                    context['unit_cost'] = unit_cost
                    context['unit_count'] = unit_count
                print("Wczytanie Units")
                for skill in user_skills:
                    skill_price.append(skill.skill_cost)
                    skill_count.append(skill.skill_count)
                    context['skill_price'] = skill_price
                    context['skill_count'] = skill_count
                print("Wczytanie Skills")
                for passive in user_passives:
                    passive_cost.append(passive.passive_cost)
                    passive_count.append(passive.passive_count)
                    context['passive_cost'] = passive_cost
                    context['passive_count'] = passive_count
                print("Wczytanie passives")
                skill_price = []
                skill_count = []
                unit_cost = []
                unit_count = []
                passive_cost = []
                passive_count = []
                return JsonResponse(context, status=200)
            else:
                print('Pierwsze logowanie : Load')
                if userCookies is None:
                    try:
                        cookie_user = Cookies(cookies_id = userCookie, current_gold = 999999, click_count=0, stage=1, stage_passed=1, click_upgrades_bought=1, var_o=-1, clickUpgradePrice=100, visibleUpgrades=-1, current_passive_points=0, current_mana=100,max_mana=100 )
                        cookie_user.save()
                        print('tworzenie usera przy load')
                    except:
                        pass
                    try:
                        cookie_user =  Cookies.objects.get(cookies_id = userCookie)
                        print('sprawdzanie usera przy load')
                    except:
                        cookie_user = None
                if user_units is None:
                    for unit in unitsCount:
                        user_units = UserUnits(cookies_id=cookie_user, unit_type = unit.unit_name, unit_cost = unit.unit_default_cost, unit_count = unit.unit_count)
                        user_units.save()
                    print('tworzenie units przy load')
                    try:
                        user_units = UserUnits.objects.filter(cookies_id = cookie_user)
                    except:
                        user_units = None
                if user_skills is None:
                    for skill in skillsCount:
                        user_skills = UserSkills(cookies_id=cookie_user, skill_type = skill.skill_name, skill_cost = skill.skill_cost, skill_count = skill.skill_count)
                        user_skills.save()
                    print('tworzenie skills przy load')
                    try:
                        user_skills = UserSkills.objects.filter(cookies_id = cookie_user)
                    except:
                        user_skills = None
                if user_passives is None:
                    for x in range(0,10):
                        user_passives = UserPassives(cookies_id = cookie_user, passive_id="passive"+str(x), passive_count = 0, passive_cost = 0)
                        user_passives.save()
                    print('tworzenie passives przy load')
                    try:
                        user_passives = UserPassives.objects.filter(cookies_id = cookie_user)
                    except:
                        user_passives = None
                context = {
                    'visibleUpgrades' : cookie_user.visibleUpgrades,
                    'var_o': cookie_user.var_o,
                    'click_count': cookie_user.click_count,
                    'stage': cookie_user.stage,
                    'stage_passed': cookie_user.stage_passed,
                    'current_gold': cookie_user.current_gold,
                    'click_upgrades_bought': cookie_user.click_upgrades_bought,
                    'clickUpgradePrice':cookie_user.clickUpgradePrice,
                    'current_passive_points':cookie_user.current_passive_points,
                    'current_mana':cookie_user.current_mana,
                    'max_mana':cookie_user.max_mana
                    }
                print("Wczytanie Usera")
                for unit in user_units:
                    unit_cost.append(unit.unit_cost)
                    unit_count.append(unit.unit_count)
                    context['unit_cost'] = unit_cost
                    context['unit_count'] = unit_count
                print("Wczytanie Units")
                for skill in user_skills:
                    skill_price.append(skill.skill_cost)
                    skill_count.append(skill.skill_count)
                    context['skill_price'] = skill_price
                    context['skill_count'] = skill_count
                print("Wczytanie Skills")
                for passive in user_passives:
                    passive_cost.append(passive.passive_cost)
                    passive_count.append(passive.passive_count)
                    context['passive_cost'] = passive_cost
                    context['passive_count'] = passive_count
                print("Wczytanie passives")
                skill_price = []
                skill_count = []
                unit_cost = []
                unit_count = []
                passive_cost = []
                passive_count = []
                return JsonResponse(context, status=200)
    except:
        pass
    context={}
    template="index.html"
    return render(request, template, context)

def coppy(request):
    template="index.html"

    if request.method == 'POST':
        current = request.POST.get('current_id')
        new = request.POST.get('new_id')
        try:
            get_user = Cookies.objects.get(cookies_id = current)
        except:
            get_user = None
        try:
            get_new_user = Cookies.objects.get(cookies_id = new)
        except:
            get_new_user = None
        try:
            new_user_skills = UserSkills.objects.filter(cookies_id = get_new_user)
        except:
            new_user_skills = None
        try:
            new_user_passives = UserPassives.objects.filter(cookies_id = get_new_user)
        except:
            new_user_passives = None
        try:
            new_user_units = UserUnits.objects.filter(cookies_id = get_new_user)
        except:
            new_user_units = None
            
        if new == '' or current == '':
            return JsonResponse({'message':'Please enter ID', 'loaded':'false',}, status=200)
        elif get_user == None or get_new_user == None:
            return JsonResponse({'message':'Cannot Find ID', 'loaded':'false',}, status=200)
        elif new_user_skills is not None and new_user_units is not None and new_user_passives is not None:
            user_units = UserUnits.objects.filter(cookies_id = get_user)
            user_skills = UserSkills.objects.filter(cookies_id = get_user)
            user_passives = UserPassives.objects.filter(cookies_id = get_user)
            if new == new_user_units[0].cookies_id.cookies_id and new == new_user_skills[0].cookies_id.cookies_id:
                get_user.current_gold = get_new_user.current_gold
                get_user.max_mana = get_new_user.max_mana
                get_user.current_mana = get_new_user.current_mana
                get_user.current_passive_points =  get_new_user.current_passive_points
                get_user.click_count = get_new_user.click_count
                get_user.stage = get_new_user.stage
                get_user.stage_passed = get_new_user.stage_passed
                get_user.click_upgrades_bought = get_new_user.click_upgrades_bought
                get_user.var_o = get_new_user.var_o
                get_user.clickUpgradePrice = get_new_user.clickUpgradePrice
                get_user.visibleUpgrades = get_new_user.visibleUpgrades
                get_user.save()
                pomocnicza = 0
                for skill in user_skills:
                    skill.skill_type = new_user_skills[pomocnicza].skill_type
                    skill.skill_cost = new_user_skills[pomocnicza].skill_cost
                    skill.skill_count = new_user_skills[pomocnicza].skill_count
                    skill.save()
                    pomocnicza = pomocnicza + 1
                pomocnicza = 0
                for unit in user_units:
                    unit.unit_type = new_user_units[pomocnicza].unit_type
                    unit.unit_cost = new_user_units[pomocnicza].unit_cost
                    unit.unit_count = new_user_units[pomocnicza].unit_count
                    unit.save()
                    pomocnicza = pomocnicza + 1
                pomocnicza = 0
                for passive in user_passives:
                    passive.passive_id = new_user_passives[pomocnicza].passive_id
                    passive.passive_count = new_user_passives[pomocnicza].passive_count
                    passive.passive_cost =  new_user_passives[pomocnicza].passive_cost
                    passive.save()
                    pomocnicza = pomocnicza + 1
                pomocnicza = 0
                    
                return JsonResponse({'message':'Loading...', 'loaded':'true',}, status=200)
            else:
                return JsonResponse({'message':'Cannot find ID', 'loaded':'false',}, status=200)
        else:
            return JsonResponse({'message':'Cannot find ID', 'loaded':'false',}, status=200)
        
    context={}
    return render(request, template, context)
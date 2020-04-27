from django.db import models

# Create your models here.

class Cookies(models.Model):
    cookies_id = models.CharField(max_length=50, default="X")
    current_gold = models.FloatField(default=0)
    click_count = models.FloatField(default=0)
    stage = models.FloatField(default=1)
    stage_passed = models.FloatField(default=1)
    click_upgrades_bought = models.FloatField(default=1)
    var_o = models.FloatField(default=-1)
    clickUpgradePrice = models.FloatField(default=100)
    visibleUpgrades = models.FloatField(default=-1)
    
    def __str__(self):
        return self.cookies_id

class UserUnits(models.Model):
    cookies_id = models.ForeignKey("Cookies", on_delete=models.CASCADE)
    unit_type = models.CharField(max_length=50, default="X")
    unit_cost = models.FloatField(default=0)
    unit_count = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.cookies_id)+' |type| '+self.unit_type
    
class UserSkills(models.Model):
    cookies_id = models.ForeignKey("Cookies", on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=50, default="X")
    skill_cost = models.FloatField(default=0)
    skill_count = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.cookies_id)+' |type| '+self.skill_type

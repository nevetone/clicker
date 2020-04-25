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
    
    def __str__(self):
        return self.cookies_id
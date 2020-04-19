from django.db import models

# Create your models here.

class Units(models.Model):
    unit_name = models.CharField(max_length=50)
    unit_id = models.CharField(max_length=50, default='xyz')
    unit_default_cost = models.IntegerField(default=0)
    unit_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.unit_name
    
class Mobs(models.Model):
    mob_name = models.CharField(max_length=50)
    mob_default_hp = models.IntegerField()
    
    def __str__(self):
        return self.mob_name
    
    

class Islands(models.Model):
    island_name = models.CharField(max_length=50)
    units = models.ManyToManyField("database.Mobs")
    boss = models.ForeignKey("database.Mobs", on_delete=models.CASCADE, related_name="boss")
    
    def __str__(self):
        return self.island_name
    
from django.db import models

# Create your models here.

class Units(models.Model):
    unit_name = models.CharField(max_length=50)
    unit_id = models.IntegerField(default=0)
    unit_default_cost = models.IntegerField(default=0)
    unit_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.unit_name
    
class Mobs(models.Model):
    mob_name = models.CharField(max_length=50)
    mob_default_hp = models.IntegerField()
    mob_image = models.ImageField(upload_to='mobs/', default=None)
    
    def __str__(self):
        return self.mob_name
    
    

class Islands(models.Model):
    island_name = models.CharField(max_length=50)
    ends = models.IntegerField(default=1)
    units = models.ManyToManyField("database.Mobs")
    boss = models.ForeignKey("database.Mobs", on_delete=models.CASCADE, related_name="boss")
    island_image = models.ImageField(upload_to='islands/', default=None)
    
    class Meta:
        ordering = ['ends']
    
    def __str__(self):
        return self.island_name
    
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=50) 
    skill_id = models.IntegerField(default=0)
    skill_cost = models.IntegerField(default=0)
    skill_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['skill_cost']
    
    def __str__(self):
        return self.skill_name
    
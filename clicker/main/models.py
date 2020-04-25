from django.db import models

# Create your models here.

class Cookies(models.Model):
    cookies_id = models.CharField(max_length=50, default="X")
    
    def __str__(self):
        return self.cookies_id
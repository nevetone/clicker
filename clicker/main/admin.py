from django.contrib import admin
from .models import Cookies, UserUnits , UserSkills, UserPassives
# Register your models here

admin.site.register(Cookies)
admin.site.register(UserUnits)
admin.site.register(UserSkills)
admin.site.register(UserPassives)
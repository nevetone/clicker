from django import forms
from django.forms import ModelForm
from .models import Cookies

class CookiesForm(ModelForm):
    class Meta:
        model = Cookies
        fields = ['cookies_id']
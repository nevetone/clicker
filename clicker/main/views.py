from django.shortcuts import render

# Create your views here.

def home(request):
    template="index.html"
    context={
        
    }
    return render(request, template, context)
    

def test(request):
    template="test.html"
    context={
        
    }
    return render(request, template, context)
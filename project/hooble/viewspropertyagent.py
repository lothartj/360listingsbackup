from django.shortcuts import render

# Create your views here.
def propertyagent(request):
    return render(request, 'propertyagent.html')
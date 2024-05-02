from django.shortcuts import render

# Create your views here.
def propertytype(request):
    return render(request, 'propertytype.html')
from django.shortcuts import render

# Create your views here.
def propertylist(request):
    return render(request, 'propertylist.html')
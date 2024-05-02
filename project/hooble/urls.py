from django.contrib import admin
from django.urls import path
from .views import index
from .viewsabout import about
from .viewspropertylist import propertylist
from .viewspropertytype import propertytype
from .viewspropertyagent import propertyagent
from .viewstestimonial import testimonial
from . viewsfourzerofour import fourzerofour
from .viewscontact import contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('propertylist/', propertylist, name='propertylist'),
    path('propertytype/', propertytype, name='propertytype'),
    path('propertyagent/', propertyagent, name='propertyagent'),
    path('testimonial/', testimonial, name='testimonial'),
    path('fourzerofour/', fourzerofour, name='fourzerofour'),
    path('contact/', contact, name='contact'),
]





from django.urls import path   #6
from . import views  #7

urlpatterns = [  #8
    path('', views.index, name='index'),# www.site.com/pages/
    path('about', views.about, name='about'),# www.site.com/pages/about
]
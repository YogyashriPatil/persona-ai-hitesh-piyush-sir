from django.urls import path
from .views import home, hiteshsir_view ,piyushsir_view
urlpatterns = [
    path('', home, name='home'), 
    path('hiteshsir_view/', hiteshsir_view, name='hiteshsir_view'),
    path('piyushsir_view/', piyushsir_view, name='piyushsir_view'),
]

from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home ),
    path('led', views.led_form, name= 'led_form'),
    path('show_led/<led_id>', views.show_led, name= 'show_led'),
    path('get_last_primary_key/', views.get_last_primary_key, name='get_last_primary_key'),
    path('show_led_result/<led_id>', views.show_led_result, name= 'show_led_result'),
]
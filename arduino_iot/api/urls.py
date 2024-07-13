from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home ),
    path('led', views.led_form, name= 'led_form'),
    path('show_led/<led_id>', views.show_led, name= 'show_led'),
    path('get_last_primary_key/', views.get_last_primary_key, name='get_last_primary_key'),
    path('show_led_result/<led_id>', views.show_led_result, name= 'show_led_result'),
    path('led_result/<led_id>', views.led_result, name= 'led_result'),
    path('simulation_list', views.simulation_list, name= 'simulation_list'),
    path('simulation_result/<led_id>', views.simulation_result, name= 'simulation_result'),
    path('simulation_pk/<led_id>', views.simulation_pk, name= 'simulation_pk'),
]
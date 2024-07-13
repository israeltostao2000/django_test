from django.db import models

# Create your models here.

class Simulation(models.Model):
    key = models.IntegerField('Led key')
    led_status = models.IntegerField('Led Status')
    time = models.IntegerField('Led Time')

    def __str__(self):
        return f"Simulation {self.key}"
    
    class Meta:
        verbose_name_plural = "Simulation"


class LedResult(models.Model):
    key = models.IntegerField('Led key')
    times_on = models.IntegerField('Times ON')
    times_off = models.IntegerField('Times OFF')
    number_cycle = models.IntegerField('Number of Cycles')
    simulation_time = models.IntegerField('Simulation time')
    
    def __str__(self):
        return f"LedResult {self.key}"
    
    class Meta:
        verbose_name_plural = "Led Result"



class Led(models.Model):
    title = models.CharField('Led Title', max_length=100, default= 'Untitled')
    time_on = models.IntegerField('Time ON')
    time_off = models.IntegerField('Time OFF')
    simulation_time = models.IntegerField('Simulation time')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Led"
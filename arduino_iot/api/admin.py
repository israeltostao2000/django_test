from django.contrib import admin

# Register your models here.
from .models import Led, LedResult

admin.site.register(Led)
admin.site.register(LedResult)
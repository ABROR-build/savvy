from django.contrib import admin
from . import models


class StationaryActivityAdmin(admin.ModelAdmin):
    list_display = ['staff', 'stationary', 'stationary_count', 'price', 'total_price', 'comment', 'time_sold']


admin.site.register(models.Stationaries)
admin.site.register(models.StationaryCategories)
admin.site.register(models.StationaryActivity, StationaryActivityAdmin)

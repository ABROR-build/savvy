from django.contrib import admin
from . import models


class StationaryActivityAdmin(admin.ModelAdmin):
    list_display = ['staff', 'stationary', 'stationary_count', 'price', 'total_price', 'comment', 'time_sold']


class StattionaryIncomeAdmin(admin.ModelAdmin):
    list_display = ['staff', 'date', 'minus', 'comment_minus', 'plus', 'comment_plus', 'total_budget']


admin.site.register(models.Stationaries)
admin.site.register(models.StationaryCategories)
admin.site.register(models.StationaryActivity, StationaryActivityAdmin)
admin.site.register(models.StationaryIncome, StattionaryIncomeAdmin)

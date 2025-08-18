from django.contrib import admin
from . import models


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['staff', 'time', 'service', 'service_count', 'price', 'total_price', 'comment']


class CustomActivityAdmin(admin.ModelAdmin):
    list_display = ['staff', 'time', 'service', 'service_count', 'price', 'total_price', 'comment']

class ExpensesAdmin(admin.ModelAdmin):
    list_diplay = ['staff', 'time', 'item', 'item_count', 'price', 'total_price', 'comment']

class DailyBudgetAdmin(admin.ModelAdmin):
    list_display = ['staff', 'date', 'minus', 'comment_minus', 'plus', 'comment_plus', 'total_budget']


class CompanyDailyBudgetAdmin(admin.ModelAdmin):
    list_display = ['day', 'budget']


class MonthlyBudgetAdmin(admin.ModelAdmin):
    list_display = ['year', 'month', 'budget']


admin.site.register(models.Services, ServiceAdmin)
admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.CustomActivity, CustomActivityAdmin)
admin.site.register(models.Expenses, ExpensesAdmin)
admin.site.register(models.DailyBudget, DailyBudgetAdmin)
admin.site.register(models.CompanyDailyBudget, CompanyDailyBudgetAdmin)
admin.site.register(models.CompanyMonthlyBudget, MonthlyBudgetAdmin)

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone

from service import models
from staff.models import Staff
from stationaries.models import StationaryActivity


class ListTodayActivities(View):
    def get(self, request):
        if request.user.is_staff:
            today = timezone.localtime()
            activities = models.Activity.objects.filter(time__date=today.date())
            custom_activities = models.CustomActivity.objects.filter(time__date=today.date())
            stationaries = StationaryActivity.objects.filter(time_sold__date=today.date())

            # budgets
            total_budget = models.CompanyDailyBudget.objects.filter(day=today.date())
            activity_total = models.DailyBudget.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                 'total_budget__sum'] or 0
            stationary_total = models.StationaryIncome.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                   'total_budget__sum'] or 0

            context = {
                'activities': activities,
                'custom_activities': custom_activities,
                'stationaries': stationaries,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }
            return render(request, 'adminka/homepage.html', context=context)
        else:
            return redirect('Login')


class FilterServices(View):
    def get(self, request):
        if request.user.is_staff:
            today = timezone.localtime()
            activities = models.Activity.objects.filter(time__date=today.date())
            custom_activities = models.CustomActivity.objects.filter(time__date=today.date())

            # budgets
            total_budget = models.CompanyDailyBudget.objects.filter(day=today.date())
            activity_total = models.DailyBudget.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                 'total_budget__sum'] or 0
            stationary_total = models.StationaryIncome.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                   'total_budget__sum'] or 0

            context = {
                'activities': activities,
                'custom_activities': custom_activities,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }

            return render(request, 'adminka/filter_service.html', context=context)
        else:
            return redirect('Login')


class FilterStationaries(View):
    def get(self, request):
        if request.user.is_staff:
            today = timezone.localtime()
            stationaries = StationaryActivity.objects.filter(time_sold__date=today.date())

            # budgets
            total_budget = models.CompanyDailyBudget.objects.filter(day=today.date())
            activity_total = models.DailyBudget.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                 'total_budget__sum'] or 0
            stationary_total = models.StationaryIncome.objects.filter(date=today.date()).aggregate(Sum('total_budget'))[
                                   'total_budget__sum'] or 0

            context = {
                'stationaries': stationaries,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }

            return render(request, 'adminka/filter_stationaries.html', context=context)
        else:
            return redirect('Login')


class FilterByUser(View):
    def get(self, request, username):
        if request.user.is_staff:
            staff = Staff.objects.filter(username=username)[:1].get()  # this line is called slicing
            today = timezone.localtime()
            activities = models.Activity.objects.filter(staff=staff, time__date=today.date())
            custom_activities = models.CustomActivity.objects.filter(staff=staff, time__date=today.date())
            stationaries = StationaryActivity.objects.filter(staff=staff, time_sold__date=today.date())

            # budgets
            activity_total = \
                models.DailyBudget.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                    'total_budget__sum'] or 0
            stationary_total = \
                models.StationaryIncome.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                    'total_budget__sum'] or 0
            total_budget = activity_total + stationary_total

            context = {
                'staff': staff,
                'activities': activities,
                'custom_activities': custom_activities,
                'stationaries': stationaries,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }

            return render(request, 'adminka/filter_by_user.html', context=context)
        else:
            return redirect('Login')


class FilterServicesByUser(View):
    def get(self, request, username):
        if request.user.is_staff:
            staff = Staff.objects.filter(username=username)[:1].get()  # this line is called slicing
            today = timezone.localtime()
            activities = models.Activity.objects.filter(staff=staff, time__date=today.date())
            custom_activities = models.CustomActivity.objects.filter(staff=staff, time__date=today.date())

            # budgets
            activity_total = \
            models.DailyBudget.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                'total_budget__sum'] or 0
            stationary_total = \
            models.StationaryIncome.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                'total_budget__sum'] or 0
            total_budget = activity_total + stationary_total

            context = {
                'staff': staff,
                'activities': activities,
                'custom_activities': custom_activities,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }

            return render(request, 'adminka/filter_service_by_user.html', context=context)
        else:
            return redirect('Login')


class FilterStationariesByUser(View):
    def get(self, request, username):
        if request.user.is_staff:
            staff = Staff.objects.filter(username=username)[:1].get()  # this line is called slicing
            today = timezone.localtime()
            stationaries = StationaryActivity.objects.filter(staff=staff, time_sold__date=today.date())

            # budgets
            activity_total = \
                models.DailyBudget.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                    'total_budget__sum'] or 0
            stationary_total = \
                models.StationaryIncome.objects.filter(staff=staff, date=today.date()).aggregate(Sum('total_budget'))[
                    'total_budget__sum'] or 0
            total_budget = activity_total + stationary_total

            context = {
                'stationaries': stationaries,
                'staff': staff,
                'total_budget': total_budget,
                'activity_total': activity_total,
                'stationary_total': stationary_total,
            }

            return render(request, 'adminka/filter_stationaries_by_user.html', context=context)
        else:
            return redirect('Login')

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone

from service import models
from staff.models import Staff
from stationaries.models import StationaryActivity

from . import forms


# Current day||||
# ///// READ CLASSES BELOW
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


# ///// UPDATE CLASSES BELOW
class EditActivity(View):
    def get(self, request, pk):
        if request.user.is_staff:
            activity = models.Activity.objects.get(pk=pk)
            activity_edit_form = forms.EditActivityForm(instance=activity)
            context = {
                'activity_edit_form': activity_edit_form
            }
            return render(request, 'adminka/edit_activity.html', context=context)
        else:
            return redirect('Login')

    def post(self, request, pk):
        if request.user.is_staff:
            today = timezone.localtime()
            activity = models.Activity.objects.get(pk=pk)
            activity_previous = models.Activity.objects.get(pk=pk)
            activity_edit_form = forms.EditActivityForm(request.POST, instance=activity)
            if activity_edit_form.is_valid():
                activity = activity_edit_form.save(commit=False)
                activity.save()

                daily_budget = models.DailyBudget.objects.get(staff=activity.staff, date=today)
                daily_budget.total_budget += (activity.total_price - activity_previous.total_price)
                daily_budget.save()

                return redirect('list-todays-activities')
        else:
            return redirect('Login')


class EditCustomActivity(View):
    def get(self, request, pk):
        if request.user.is_staff:
            custom_activity = models.CustomActivity.objects.get(pk=pk)
            custom_activity_edit_form = forms.EditCustomActivityForm(instance=custom_activity)
            context = {
                'custom_activity_edit_form': custom_activity_edit_form
            }
            return render(request, 'adminka/edit_custom_activity.html', context=context)
        else:
            return redirect('Login')

    def post(self, request, pk):
        if request.user.is_staff:
            today = timezone.localtime()
            custom_activity = models.CustomActivity.objects.get(pk=pk)
            custom_activity_previous = models.CustomActivity.objects.get(pk=pk)
            custom_activity_edit_form = forms.EditCustomActivityForm(request.POST, instance=custom_activity)
            if custom_activity_edit_form.is_valid():
                custom_activity = custom_activity_edit_form.save(commit=False)
                custom_activity.save()

                daily_budget = models.DailyBudget.objects.get(staff=custom_activity.staff, date=today)
                daily_budget.total_budget += (custom_activity.total_price - custom_activity_previous.total_price)
                daily_budget.save()

                return redirect('list-todays-activities')
        else:
            return redirect('Login')

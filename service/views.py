# global
from datetime import date
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views import View

# local
from . import models
from . import forms


class ListServices(View):
    def get(self, request):
        services = models.Services.objects.all()
        context = {
            'services': services
        }
        return render(request, 'service/services.html', context=context)


class PostService(View):
    def get(self, request, pk):
        service = models.Services.objects.get(pk=pk)
        activity_form = forms.ActivityForm(initial={'service': service, 'price': service.price})

        activities = models.Activity.objects.filter(staff=request.user)
        daily_budgets = models.DailyBudget.objects.filter(staff=request.user)

        context = {
            'service': service,
            'activity_form': activity_form,
            'activities': activities,
            'daily_budgets': daily_budgets,
        }
        return render(request, 'service/post_service.html', context=context)

    def post(self, request, pk):
        activity_form = forms.ActivityForm(request.POST)

        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.staff = request.user
            activity.save()

            daily_budget, created = models.DailyBudget.objects.get_or_create(staff=request.user, date=date.today())
            daily_budget.save()
            daily_budget = models.DailyBudget.objects.get(staff=request.user, date=date.today())
            daily_budget.total_budget += activity.total_price
            daily_budget.save()

            if not created:
                # daily_budget.total_budget += activity.total_price
                daily_budget.save()

            return redirect('list_services')
        else:
            print('Not valid')
            return render(request, 'service/post_service.html', {'activity_form': activity_form})


class PostCustomService(View):
    def get(self, request):
        activity_form = forms.CustomActivity()
        context = {
            'custom_activity_form': activity_form
        }
        return render(request, 'service/post_new_service.html', context=context)

    def post(self, request):
        activity_form = forms.CustomActivityForm(request.POST)
        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.staff = request.user
            activity.save()

            daily_budget, created = models.DailyBudget.objects.get_or_create(staff=request.user, date=date.today())
            daily_budget.save()
            daily_budget = models.DailyBudget.objects.get(staff=request.user, date=date.today())
            daily_budget.total_budget += activity.total_price
            daily_budget.save()

            if not created:
                # daily_budget.total_budget += activity.total_price
                daily_budget.save()

            return redirect('list_services')
        else:

            context = {
                'custom_activity_form': activity_form
            }
            return render(request, 'service/post_new_service.html', context=context)


class ListMyActivities(View):
    def get(self, request):
        today = timezone.localtime()
        activities = models.Activity.objects.filter(staff=request.user, time__date=today.date())
        custom_activities = models.CustomActivity.objects.filter(staff=request.user, time__date=today.date())
        daily_budget = models.DailyBudget.objects.filter(staff=request.user, date=today)
        context = {
            'activities': activities,
            'custom_activities': custom_activities,
            'daily_budget': daily_budget
        }
        print(daily_budget)
        return render(request, 'service/my_activities.html', context=context)

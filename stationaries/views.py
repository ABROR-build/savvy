from django.views import View
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date

from . import models
from . import forms


class ListCategories(View):
    def get(self, request):
        categories = models.StationaryCategories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'stationaries/list_categories.html', context=context)


class ListStationaries(View):
    def get(self, request):
        stationaries = models.Stationaries.objects.all()
        context = {
            'stationaries': stationaries
        }
        return render(request, 'stationaries/list_stationaries.html', context=context)


class FilterStationaries(View):
    def get(self, request, pk):
        stationaries = models.Stationaries.objects.filter(category=pk)
        context = {
            'stationaries': stationaries
        }
        return render(request, 'stationaries/filter_stationaries.html', context=context)


class SellStationary(View):
    def get(self, request, pk):
        stationary = models.Stationaries.objects.get(pk=pk)
        sell_form = forms.StationaryActivityForm(initial={'stationary': stationary, 'price': stationary.price})
        context = {
            'stationary': stationary,
            'sell_form': sell_form
        }
        return render(request, 'stationaries/sell_stationaries.html', context=context)

    def post(self, request, pk):
        sell_form = forms.StationaryActivityForm(request.POST)
        if sell_form.is_valid():
            stationary_activity = sell_form.save(commit=False)
            stationary_activity.staff = request.user
            stationary_activity.save()

            stationary_income, created = models.StationaryIncome.objects.get_or_create(staff=request.user,
                                                                                       date=date.today())
            stationary_income.save()

            stationary_income = models.StationaryIncome.objects.get(staff=request.user, date=date.today())
            stationary_income.total_budget += stationary_activity.price
            stationary_income.save()

            return redirect('list-stationaries')

        else:
            context = {
                'sell_form': sell_form
            }
            return render(request, 'stationaries/sell_stationaries.html', context=context)


class ListSell(View):
    def get(self, request):
        today = timezone.localtime()
        sells = models.StationaryActivity.objects.filter(
            staff=request.user, time_sold__date=today.date()
        )

        context = {
            'sells': sells
        }
        return render(request, 'stationaries/list_sell.html', context=context)

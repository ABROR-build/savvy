from django.views import View
from django.shortcuts import render, redirect

from . import models


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

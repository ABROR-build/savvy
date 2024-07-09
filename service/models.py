from django.db import models
from staff.models import Staff
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


class Services(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()

    class Meta:
        db_table = 'Services'

    def __str__(self):
        return self.name


class Activity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    service_count = models.PositiveIntegerField(default=1)
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)  # New field
    comment = models.CharField(max_length=800, null=True, blank=True)
    total_price = models.IntegerField(default=0)

    def calculate_price(self):
        return self.price * self.service_count

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "Activity"


class CustomActivity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    service = models.CharField(max_length=800)
    service_count = models.PositiveIntegerField(default=1)
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)  # New field
    comment = models.CharField(max_length=800, null=True, blank=True)
    total_price = models.IntegerField(default=0)

    def calculate_price(self):
        return self.price * self.service_count

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "CustomActivity"


class DailyBudget(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    minus = models.IntegerField(default=0)
    comment_minus = models.CharField(max_length=500, null=True, blank=True)
    plus = models.IntegerField(default=0)
    comment_plus = models.CharField(max_length=500, null=True, blank=True)
    original = models.IntegerField(default=0)
    total_budget = models.IntegerField(default=0)

    def get_original(self):
        return self.total_budget + 0

    def edit(self):
        return (self.total_budget + self.plus) - self.minus

    def save(self, *args, **kwargs):
        self.original = self.get_original()
        self.total_budget = self.edit()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "DailyBudget"


class CompanyDailyBudget(models.Model):
    day = models.DateField(auto_now=True)
    budget = models.IntegerField()

    @receiver(post_save, sender=DailyBudget)
    @receiver(post_delete, sender=DailyBudget)
    def update_company_daily_budget(sender, instance, **kwargs):
        day = instance.date
        total_budget_sum = DailyBudget.objects.filter(date=day).aggregate(Sum('total_budget'))['total_budget__sum'] or 0
        CompanyDailyBudget.objects.update_or_create(day=day, defaults={'budget': total_budget_sum})

    class Meta:
        db_table = "CompanyDailyBudget"


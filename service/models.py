from django.db import models
from staff.models import Staff
from stationaries.models import StationaryIncome

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

# services
class Services(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()

    class Meta:
        db_table = 'Services'

    def __str__(self):
        return self.name

# activity
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

# custom activity
class CustomActivity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    service = models.CharField(max_length=800)
    service_count = models.PositiveIntegerField(default=1)
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    comment = models.CharField(max_length=800, null=True, blank=True)
    total_price = models.IntegerField(default=0)

    def calculate_price(self):
        return self.price * self.service_count

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "CustomActivity"

# expenses
class Expenses(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    item = models.CharField(max_length=800)
    item_count = models.PositiveIntegerField(default=1)
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    comment = models.CharField(max_length=800, null=True, blank=True)
    total_price = models.IntegerField(default=0)

    def calculate_price(self):
        return self.price * self.item_count

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "Expenses"

# daily budegt
class DailyBudget(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    minus = models.IntegerField(default=0)
    comment_minus = models.CharField(max_length=500, null=True, blank=True)
    plus = models.IntegerField(default=0)
    comment_plus = models.CharField(max_length=500, null=True, blank=True)
    total_budget = models.IntegerField(default=0)

    def edit(self):
        return (self.total_budget + self.plus) - self.minus

    def save(self, *args, **kwargs):
        self.total_budget = self.edit()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "DailyBudget"

# company daily budged
class CompanyDailyBudget(models.Model):
    day = models.DateField(auto_now=True)
    budget = models.IntegerField()

    @receiver(post_save, sender=DailyBudget)
    @receiver(post_save, sender=StationaryIncome)
    @receiver(post_delete, sender=DailyBudget)
    @receiver(post_delete, sender=StationaryIncome)
    def update_company_daily_budget(sender, instance, **kwargs):
        day = instance.date
        total_budget_sum1 = DailyBudget.objects.filter(date=day).aggregate(Sum('total_budget'))[
                                'total_budget__sum'] or 0
        total_budget_sum2 = StationaryIncome.objects.filter(date=day).aggregate(Sum('total_budget'))[
                                'total_budget__sum'] or 0
        CompanyDailyBudget.objects.update_or_create(day=day, defaults={'budget': total_budget_sum1 + total_budget_sum2})

    class Meta:
        db_table = "CompanyDailyBudget"

# company monthly budget
class CompanyMonthlyBudget(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    budget = models.IntegerField()

    @receiver(post_save, sender=CompanyDailyBudget)
    @receiver(post_delete, sender=CompanyDailyBudget)
    def update_company_monthly_budget(sender, instance, **kwargs):
        year = instance.day.year
        month = instance.day.month
        total_budget = CompanyDailyBudget.objects.filter(day__year=year, day__month=month).aggregate(Sum('budget'))['budget__sum'] or 0
        CompanyMonthlyBudget.objects.update_or_create(
            year=year,
            month=month,
            defaults={'budget': total_budget}
        )

    class Meta:
        db_table = "CompanyMonthlyBudget"
        unique_together = ("year", "month")

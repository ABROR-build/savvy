from django.db import models
from staff.models import Staff


class StationaryCategories(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'StationaryCategories'

    def __str__(self):
        return self.name


class Stationaries(models.Model):
    category = models.ForeignKey(StationaryCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='stationaries/')
    price = models.IntegerField()

    class Meta:
        db_table = "Stationaries"

    def __str__(self):
        return self.name


class StationaryActivity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    stationary = models.ForeignKey(Stationaries, on_delete=models.CASCADE)
    stationary_count = models.IntegerField(default=1)
    time_sold = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    comment = models.CharField(max_length=800, null=True, default=True)

    def calculate_price(self):
        return self.price * self.stationary_count

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "StationarActivity"

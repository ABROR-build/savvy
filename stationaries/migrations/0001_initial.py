# Generated by Django 5.0.6 on 2025-03-27 07:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stationaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='stationaries/')),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Stationaries',
            },
        ),
        migrations.CreateModel(
            name='StationaryCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'StationaryCategories',
            },
        ),
        migrations.CreateModel(
            name='StationaryActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationary_count', models.IntegerField(default=1)),
                ('time_sold', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('comment', models.CharField(default=True, max_length=800, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stationary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationaries.stationaries')),
            ],
            options={
                'db_table': 'StationarActivity',
            },
        ),
        migrations.AddField(
            model_name='stationaries',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationaries.stationarycategories'),
        ),
        migrations.CreateModel(
            name='StationaryIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('minus', models.IntegerField(default=0)),
                ('comment_minus', models.CharField(blank=True, max_length=500, null=True)),
                ('plus', models.IntegerField(default=0)),
                ('comment_plus', models.CharField(blank=True, max_length=500, null=True)),
                ('total_budget', models.IntegerField(default=0)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'StationaryIncome',
            },
        ),
    ]

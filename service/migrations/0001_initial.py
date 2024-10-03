# Generated by Django 5.0.6 on 2024-09-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_count', models.PositiveIntegerField(default=1)),
                ('time', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, max_length=800, null=True)),
                ('total_price', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Activity',
            },
        ),
        migrations.CreateModel(
            name='CompanyDailyBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now=True)),
                ('budget', models.IntegerField()),
            ],
            options={
                'db_table': 'CompanyDailyBudget',
            },
        ),
        migrations.CreateModel(
            name='CustomActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=800)),
                ('service_count', models.PositiveIntegerField(default=1)),
                ('time', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, max_length=800, null=True)),
                ('total_price', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'CustomActivity',
            },
        ),
        migrations.CreateModel(
            name='DailyBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('minus', models.IntegerField(default=0)),
                ('comment_minus', models.CharField(blank=True, max_length=500, null=True)),
                ('plus', models.IntegerField(default=0)),
                ('comment_plus', models.CharField(blank=True, max_length=500, null=True)),
                ('total_budget', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'DailyBudget',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Services',
            },
        ),
    ]

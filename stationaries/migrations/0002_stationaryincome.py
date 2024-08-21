# Generated by Django 5.0.6 on 2024-08-21 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationaries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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

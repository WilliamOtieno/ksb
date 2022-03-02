# Generated by Django 3.2.12 on 2022-02-27 08:36

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyworksheet',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dailyworksheet',
            name='date',
            field=models.DateField(default=datetime.date(2022, 2, 27)),
        ),
        migrations.AlterField(
            model_name='dailyworksheet',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 3.2.12 on 2022-02-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220227_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyworksheet',
            name='client_org',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
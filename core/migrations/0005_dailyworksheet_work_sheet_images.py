# Generated by Django 3.2.12 on 2022-02-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_dailyworksheet_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyworksheet',
            name='work_sheet_images',
            field=models.FileField(blank=True, null=True, upload_to='work_sheet/'),
        ),
    ]

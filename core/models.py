import base64

from django.conf import settings
from django.db import models
from django.utils import timezone

from authentication.models import Client, SalesPerson, Engineer, Manager


class DailyWorkSheet(models.Model):
    client = models.CharField(max_length=200, null=True)
    client_org = models.CharField(max_length=200, null=True)
    engineer = models.CharField(max_length=200, null=True)
    manager = models.CharField(max_length=200, null=True)
    report = models.TextField()
    recommendation = models.TextField()
    action_work_required = models.TextField()
    arrival_time = models.DateTimeField(default=timezone.now)
    departure_time = models.DateTimeField(default=timezone.now)
    vehicle_reg = models.CharField(max_length=10)
    start_mileage = models.IntegerField()
    end_mileage = models.IntegerField()
    location = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    department = models.CharField(max_length=300)
    job_number = models.CharField(max_length=100)
    client_signature = models.TextField()
    engineer_signature = models.TextField()
    work_sheet_images = models.FileField(null=False, blank=False, upload_to='work_sheet/')

    class Meta:
        verbose_name = 'Daily Work Sheet'
        verbose_name_plural = 'Daily Work Sheets'

    def decode_signature(self, signature_str: str):
        img_data = base64.decodestring(signature_str.encode())
        f = open(f"{settings.BASE_DIR}/output.png", "wb")
        f.write(img_data)
        f.close()

    def decode_client_sig(self):
        return self.decode_signature(self.client_signature)

    def decode_engineer_signature_sig(self):
        return self.decode_signature(self.engineer_signature)

    def get_distance(self):
        return self.end_mileage - self.start_mileage

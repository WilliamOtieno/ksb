from rest_framework import serializers
from .models import DailyWorkSheet


class DailyWorkSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyWorkSheet
        fields = '__all__'

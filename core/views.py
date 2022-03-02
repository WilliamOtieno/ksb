from django.shortcuts import render
from django.views.generic import TemplateView
from easy_pdf.rendering import render_to_pdf_response
from rest_framework import generics

from .models import DailyWorkSheet
from .serializers import DailyWorkSheetSerializer


class DailyWorkSheetCreateAPIView(generics.CreateAPIView):
    queryset = DailyWorkSheet.objects.all()
    serializer_class = DailyWorkSheetSerializer


class DailyWorkSheetRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DailyWorkSheet.objects.all()
    serializer_class = DailyWorkSheetSerializer


class DailyWorkSheetUpdateAPIView(generics.UpdateAPIView):
    queryset = DailyWorkSheet.objects.all()
    serializer_class = DailyWorkSheetSerializer


class DailyWorkSheetDeleteAPIView(generics.DestroyAPIView):
    queryset = DailyWorkSheet.objects.all()
    serializer_class = DailyWorkSheetSerializer


class DailyWorkSheetListAPIView(generics.ListAPIView):
    queryset = DailyWorkSheet.objects.all()
    serializer_class = DailyWorkSheetSerializer


def index(request):
    obj = DailyWorkSheet.objects.all().last()
    context = {
        'obj': obj
    }
    return render(request, 'index.html', context)

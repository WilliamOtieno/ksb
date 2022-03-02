from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.DailyWorkSheetCreateAPIView.as_view()),
    path('retrieve/<pk>/', views.DailyWorkSheetRetrieveAPIView.as_view()),
    path('update/<pk>/', views.DailyWorkSheetUpdateAPIView.as_view()),
    path('delete/<pk>/', views.DailyWorkSheetDeleteAPIView.as_view()),
    path('list/', views.DailyWorkSheetListAPIView.as_view()),
]

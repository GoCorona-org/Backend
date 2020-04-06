from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from corona_app import views

urlpatterns = [
    path('corona_app/', views.CoronaAppList.as_view()),
    path('corona_app/<int:pk>/', views.CoronaAppDetail.as_view()),
    path('corona_app/result/', views.CoronaAppResult.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
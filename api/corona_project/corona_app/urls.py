from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from corona_app import views

app_name = 'corona_app'

urlpatterns = [
    path('corona_app/', views.CoronaAppList.as_view()),
    path('corona_app/<int:pk>/', views.CoronaAppDetail.as_view()),
    path('corona_app/result/', views.CoronaAppResult.as_view()),
    path('corona_app/medmap/', views.MedicalMapFormView, name = 'medmap_form'),
    path('corona_app/medmap/<int:id>/', views.MedicalMapFormDetail, name = 'medmap_detail'),
    # path('corona_app/medmap/<int:pk>/score_color', views.MedicalMapScoreColor.as_view(), name = 'medmap_color'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
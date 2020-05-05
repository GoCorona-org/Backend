from rest_framework.urlpatterns import format_suffix_patterns
# from django.conf.urls import url
from django.urls import path
from medicalmap import views

app_name = 'medicalmap'

urlpatterns = [
    path('medmap/', views.MedicalList.as_view()),
    path('medmap/<str:med_uuid>/', views.MedicalDetail.as_view()),
    path('medmap/result/<str:med_uuid>/', views.MedicalResult.as_view()),
    path('medmap/list/<str:file>/', views.TravelList.as_view()),
    path('gmailAuthenticate/', views.gmail_authenticate, name ='gmail_authenticate'), 
    path('oauth2callback/', views.auth_return), 
    path('', views.home, name ='home'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)
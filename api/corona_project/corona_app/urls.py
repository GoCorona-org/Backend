from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from corona_app import views

app_name = 'corona_app'

urlpatterns = [
    path('report/', views.corona_history_list),
    path('temp_calculator/', views.CoronaAppResult.as_view()),
    path('map/<str:status>/', views.IntersectMapResult.as_view()),    
    path('amIExposed/<str:uuid>', views.UserExposure.as_view()),
    path('result/times/', views.CoronaAppTimeslots.as_view()),
    path('medmap/', views.MedicalList.as_view()),
    path('medmap/<int:pk>', views.MedicalDetail.as_view()),
    path('medmap/result/<int:pk>', views.MedicalResult.as_view()),
    # path('medmap/', views.MedicalMapFormView, name = 'medmap_form'),
    # path('medmap/<int:id>/', views.MedicalMapFormDetail, name = 'medmap_detail'),
    # path('corona_app/medmap/<int:pk>/score_color', views.MedicalMapScoreColor.as_view(), name = 'medmap_color'),
    # path('<int:pk>/', views.CoronaAppDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
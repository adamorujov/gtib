from django.urls import path
from gtib import views

app_name = "gtib"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('charter/', views.CharterView.as_view(), name="charter"),
    path('volunteer/', views.VolunteerView.as_view(), name="volunteer"),
    path('departments/', views.DepartmentsView.as_view(), name="departments"),
    path('directors/', views.DirectorsView.as_view(), name="directors"),
]
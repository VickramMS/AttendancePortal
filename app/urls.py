from django.urls import path
from . import views

urlpatterns = [
    path('', views.AttendanceView.as_view()),
    path('api/attendance', views.AddAttendanceAPI.as_view()),
]

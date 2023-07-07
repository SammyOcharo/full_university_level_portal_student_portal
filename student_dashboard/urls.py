from django.urls import path 
from . import views
urlpatterns = [
    path('student-dashboard/', views.StudentDashboardAPIView.as_view(), name='student-dashboard-api')
]
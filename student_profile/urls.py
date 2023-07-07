from django.urls import path 
from . import views
urlpatterns = [
    path('student-profile/', views.StudentProfileAPIView.as_view(), name='student-profile-api')
]
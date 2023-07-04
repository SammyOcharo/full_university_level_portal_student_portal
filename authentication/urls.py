from django.urls import path
from . import views
urlpatterns = [
    path('student-login/', views.StudentLoginAPIView.as_view(), name='student-login-api')
]
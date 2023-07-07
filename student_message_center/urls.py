from django.urls import path
from . import views
urlpatterns = [
    path('view-messages/', views.StudentViewMessageAPIView.as_view(), name='student-view-message-api')
]
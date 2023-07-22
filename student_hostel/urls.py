from django.urls import path
from . import views
urlpatterns = [
    path('apply-hostel', views.ApplyHostelAPIView.as_view(), name='apply-hostel-api'),
    path('view-hostel-details/', views.ViewHostelDetailsAPIView.as_view(), name='view-hostel-details-api')
]
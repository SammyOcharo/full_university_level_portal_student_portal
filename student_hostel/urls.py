from django.urls import path
from . import views
urlpatterns = [
    path('view-hostel-details/', views.ViewHostelDetailsAPIView.as_view(), name='view-hostel-details-api')
]
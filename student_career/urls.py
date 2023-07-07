from django.urls import path
from . import views
urlpatterns = [
    path('view-units/', views.ViewUnitsAPIView.as_view(), name='view-unit-api')
]
from django.urls import path
from . import views
urlpatterns = [
    path('send-message/', views.StudentSendMessageAPIView.as_view(), name='send-message-apiview'),
    path('view-messages/', views.StudentViewMessageAPIView.as_view(), name='student-view-message-api'),
    path('delete-message/', views.StudentDeleteMessageAPIView.as_view(), name='student-delete-message-api'),
    path('delete-thread/', views.StudentDeleteThreadAPIView.as_view(), name='delete-thread-api')
]
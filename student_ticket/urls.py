from django.urls import path

from . import views
urlpatterns = [
    path('create-ticket/', views.StudentCreateTicketAPIView.as_view(), name='student-create-ticket-api'),
    path('submit-ticket/', views.StudentSubmitTicketAPIView.as_view(), name='student-submit-ticket-api'),
    path('list-submit-ticket/', views.StudentListSubmitTicketAPIView.as_view(), name='student-list-submit-ticket-api'),
]
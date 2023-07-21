

from django.urls import path, include

urlpatterns = [
    path('apps/student/v1/auth/', include('authentication.urls')),
    path('apps/student/v1/ticket/', include('student_ticket.urls')),
    path('apps/student/v1/profile/', include('student_profile.urls')),
    path('apps/student/v1/dashboard/', include('student_dashboard.urls')),
    path('apps/student/v1/career/', include('student_career.urls')),
    path('apps/student/v1/hostel/', include('student_hostel.urls')),
    path('apps/student/v1/message/', include('student_message_center.urls')),
]

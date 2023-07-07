"""
URL configuration for student_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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

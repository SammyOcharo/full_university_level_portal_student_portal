from django.urls import path
from . import views
urlpatterns = [
    path('student-login/', views.StudentLoginAPIView.as_view(), name='student-login-api'),
    path('student-verify-login/', views.StudentVerifyLoginAPIView.as_view(), name='verify-student-login-api'),
    path('student-forgot-password/', views.StudentForgotPasswordAPIView.as_view(), name='student-forgot-password-api'),
    path('student-verify-forgot-password/', views.StudentVerifyOtpForgotPasswordAPIView.as_view(), name='student-verify-forgot-password-api'),
    path('student-new-password/', views.StudentNewPasswordAPIView.as_view(), name='student-new-password-api'),
    path('student-resend-forgot-password-otp/', views.StudentResendOtpAPIView.as_view(), name='student-resend-otp-api')
]
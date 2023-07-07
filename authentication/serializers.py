from rest_framework import serializers

class StudentLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class StudentVerifyLoginSerializer(serializers.Serializer):
   username = serializers.EmailField()
   otp = serializers.IntegerField()

class StudentForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOtpForgotPasswordSerializer(serializers.Serializer):
   email = serializers.EmailField()
   otp = serializers.IntegerField()

class StudentNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    old_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    confirm_new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class StudentResendOtpSerializer(serializers.Serializer):
   email = serializers.EmailField()
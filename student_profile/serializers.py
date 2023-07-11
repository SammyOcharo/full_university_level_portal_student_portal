from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('password',)

class StudentUpdatePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    current_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    confirm_new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
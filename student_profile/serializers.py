from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentProfileSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = '__all__'
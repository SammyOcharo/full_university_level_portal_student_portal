from rest_framework import serializers

class StudentLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class StudentVerifyLoginSerializer(serializers.Serializer):
   username = serializers.EmailField()
   otp = serializers.IntegerField()
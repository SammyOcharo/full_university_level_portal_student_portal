from rest_framework import serializers
from django.contrib.auth import get_user_model

from student_career.models import Student

User = get_user_model()

class StudentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class StudentDashboardSerializer(serializers.ModelSerializer):
    user = StudentUserSerializer()

    class Meta:
        model = Student
        fields = ('user','school_id_number', 'course', 'status', 'units')
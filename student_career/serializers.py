from rest_framework import serializers

from student_career.models import Student


class ViewUnitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('units',)
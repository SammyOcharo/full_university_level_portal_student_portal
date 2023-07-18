from rest_framework import serializers


class StudentCreateTicketSerializer(serializers.Serializer):
    message = serializers.CharField()
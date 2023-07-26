from rest_framework import serializers


class StudentSendMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    recipient = serializers.EmailField()


class StudentDeleteMessageSerializer(serializers.Serializer):
    message_id = serializers.CharField()
    thread_id = serializers.CharField()

class StudentDeleteThreadSerializer(serializers.Serializer):
    thread_id = serializers.CharField()

class StudentViewMessageSerializer(serializers.ModelSerializer):
    pass
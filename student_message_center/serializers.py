from rest_framework import serializers


class StudentSendMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    recipient = serializers.EmailField()


class StudentDeleteMessageSerializer(serializers.Serializer):
    pass

class StudentDeleteThreadSerializer(serializers.Serializer):
    pass

class StudentViewMessageSerializer(serializers.ModelSerializer):
    pass
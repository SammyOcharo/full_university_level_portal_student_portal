from rest_framework import serializers


class StudentSendMessageSerializer(serializers.Serializer):
    pass


class StudentDeleteMessageSerializer(serializers.Serializer):
    pass

class StudentDeleteThreadSerializer(serializers.Serializer):
    pass

class StudentViewMessageSerializer(serializers.ModelSerializer):
    pass
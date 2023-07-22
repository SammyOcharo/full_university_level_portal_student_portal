from rest_framework import serializers


class ApplyHostelSerializer(serializers.Serializer):
    email = serializers.EmailField()
    hostel_name = serializers.EmailField()
    hostel_room_number = serializers.CharField()
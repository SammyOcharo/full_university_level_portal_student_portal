from rest_framework import serializers

from student_ticket.models import StudentTicket


class StudentCreateTicketSerializer(serializers.Serializer):
    message = serializers.CharField()

class StudentListSubmitTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTicket
        fields = '__all__'
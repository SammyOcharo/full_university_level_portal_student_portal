from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from student_message_center.serializers import StudentDeleteMessageSerializer, StudentDeleteThreadSerializer, StudentSendMessageSerializer, StudentViewMessageSerializer

class StudentViewMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentViewMessageSerializer

class StudentSendMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSendMessageSerializer

class StudentDeleteMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentDeleteMessageSerializer


class StudentDeleteThreadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentDeleteThreadSerializer


import re
import uuid
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from student_message_center.models import StudentMessaging

from student_message_center.serializers import StudentDeleteMessageSerializer, StudentDeleteThreadSerializer, StudentSendMessageSerializer, StudentViewMessageSerializer

from django.contrib.auth import get_user_model

User = get_user_model()
class StudentViewMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentViewMessageSerializer

class StudentSendMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSendMessageSerializer

    def post(self, request):
        try:
            current_user = request.user
            data = request.data
            serializer = self.serializer_class(data=data)

            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided.',
                    'error': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            message = request.data.get('message')
            recipient = request.data.get('recipient')

            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            valid_email = re.fullmatch(email_regex, recipient)

            if not valid_email:
                return Response({
                    'status': False,
                    'message': 'Invalid email provided'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            recipient = User.objects.filter(username=recipient)
            

            if not recipient.exists():
                return Response({
                    'status': False,
                    'message': 'Recipient does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            recipient = recipient.first()
           
            
            user = User.objects.filter(username=current_user)

            thread_id = uuid.uuid4().hex
            

            if not user.exists():
                return Response({
                    'status': False,
                    'message': 'User does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()
            print(user.mobile_number)
            print(user.password)
            

            allowed_roles = ['students']
            print(user.role.short_name)

            if not user.role.short_name in allowed_roles:
                return Response({
                    'status': False,
                    'message': f'user with this role {user.role.short_name} not allowed to access this portal',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if user.status == 0:
                return Response({
                    'status': False,
                    'message': 'Student portal not yet approved please contact IT.'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if user.status == 2:
                return Response({
                    'status': False,
                    'message': 'Student portal account is suspended check in with IT'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            #save to db
            StudentMessaging(user=user, message=message, recipient=recipient, thread_id=thread_id)

            return Response({
                'status': True,
                'message': 'Message sent successfully!'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Could not send message!'
            }, status=status.HTTP_400_BAD_REQUEST)

class StudentDeleteMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentDeleteMessageSerializer

    def post(self, request):
        try:
            current_user = request.user
            data = request.data
            serializer = self.serializer_class(data=data)

            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided.',
                    'error': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            message_id = request.data.get('message_id')
            thread_id = request.data.get('thread_id')

            user = User.objects.filter(username=current_user)
                

            if not user.exists():
                return Response({
                    'status': False,
                    'message': 'User does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()
            print(user.mobile_number)
            print(user.password)
            

            allowed_roles = ['students']
            print(user.role.short_name)

            if not user.role.short_name in allowed_roles:
                return Response({
                    'status': False,
                    'message': f'user with this role {user.role.short_name} not allowed to access this portal',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if user.status == 0:
                return Response({
                    'status': False,
                    'message': 'Student portal not yet approved please contact IT.'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if user.status == 2:
                return Response({
                    'status': False,
                    'message': 'Student portal account is suspended check in with IT'
                }, status=status.HTTP_400_BAD_REQUEST)
        
            message = StudentMessaging.objects.filter(thread_id=thread_id, message_id=message_id)

            if not message.exists():
                return Response({
                    'status': False,
                    'message': 'Message does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            message = message.first()

            message.delete()

            return Response({
                'status': True,
                'message': 'Message deleted!'
            }, status=status.HTTP_200_OK)
            

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Unable to delete the message!'
            }, status=status.HTTP_400_BAD_REQUEST)


class StudentDeleteThreadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentDeleteThreadSerializer


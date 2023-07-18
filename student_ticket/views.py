import re
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()
from student_ticket.serializers import StudentCreateTicketSerializer


class StudentCreateTicketAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentCreateTicketSerializer

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
            password = request.data.get('password')

           
            
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
            
            
        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Could not submit ticket for some reason!'
            },status=status.HTTP_400_BAD_REQUEST )

class StudentSubmitTicketAPIView(APIView):
    pass

class StudentListSubmitTicketAPIView(APIView):
    pass
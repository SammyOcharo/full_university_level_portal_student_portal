import re
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from student_hostel.models import Hostel

from student_hostel.serializers import ApplyHostelSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class ApplyHostelAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplyHostelSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)

            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided.',
                    'error': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            email = request.data.get('email')
            hostel_name = request.data.get('hostel_name')
            hostel_room_number = request.data.get('hostel_room_number')

            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            valid_email = re.fullmatch(email_regex, email)

            if not valid_email:
                return Response({
                    'status': False,
                    'message': 'Invalid email provided'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.filter(username=email)
            

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
            
            import datetime

            # Get the current date and time
            current_datetime = datetime.datetime.now()

            # Print the current date and time
            print("Current date and time:", current_datetime)

            four_months_later = current_datetime + datetime.timedelta(days=4*30)  # Assuming 30 days per month

            
            Hostel.objects.create(user=user, hostel_name=hostel_name, hostel_room_number=hostel_room_number, hostel_entry=current_datetime, hostel_exit=four_months_later)


            return Response({
                'status': True,
                'status': 'Application successful!'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Could not apply for hostel!'
            }, status=status.HTTP_400_BAD_REQUEST)

class ViewHostelDetailsAPIView(APIView):
    pass
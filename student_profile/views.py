import re
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()

from student_profile.serializers import StudentProfileSerializer, StudentUpdatePasswordSerializer

class StudentProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentProfileSerializer

    def get(self, request):
        try:
            current_user = request.user
            print(current_user)

            allowed_roles = ['students']

            user = User.objects.filter(email=current_user)

            if not user.exists():
                return Response({
                    'status': False,
                    'message': 'User does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()
            
            allowed_roles = ['students']
            if not user.role.short_name in allowed_roles:
                return Response({
                    'status': False,
                    'message': f'user with this role {user.role.short_name} not allowed to access this portal',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.serializer_class(user)

            return Response({
                'status': True,
                'message': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Could not view profile'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class StudentChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentUpdatePasswordSerializer 
    
    def post(self, request):
        try:
            current_user = request.user
            print(current_user)

            allowed_roles = ['students']

            user = User.objects.filter(email=current_user)

            if not user.exists():
                return Response({
                    'status': False,
                    'message': 'User does not exist'
                }, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()
            
            allowed_roles = ['students']
            if not user.role.short_name in allowed_roles:
                return Response({
                    'status': False,
                    'message': f'user with this role {user.role.short_name} not allowed to access this portal',
                }, status=status.HTTP_400_BAD_REQUEST)
                
            data = request.data
            
            serializer = self.serializer_class(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            email = request.data.get('email')
            current_password = request.data.get('current_password')
            new_password = request.data.get('new_password')
            confirm_new_password = request.data.get('confirm_new_password')
            
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            valid_email = re.fullmatch(email_regex, email)
            if not valid_email:
                return Response({
                    'status': False,
                    'message': 'Provide a valid email to continue'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            user = User.objects.filter(email=email)
            user = user.first()

            print(current_password)
            
            password_match = user.check_password(current_password)
            
            print('password_match: ', password_match)
            if not password_match:
                return Response({
                    'status': False,
                    'message': 'Current Password Mismatch'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if len(new_password) < 8:
                return Response({
                    'status': False,
                    'message': 'Password should contain 8 or more characters',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if current_password == new_password:
                return Response({
                    'status': False,
                    'message': 'Password Reuse is not allowed'
                }, status=status.HTTP_400_BAD_REQUEST)
            #comment
            if new_password != confirm_new_password:
                return Response({
                    'status': False,
                    'message': 'Mismatch in new and confirm password'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            user.set_password(new_password)
            user.save()
            return Response({
                'status': True,
                'message': 'Password updated successfully'
            }, status=status.HTTP_200_OK)
            
        except Exception as error:
            print(str(error))
            
            return Response({
                'status': False,
                'message': 'Could not update password'
            }, status=status.HTTP_400_BAD_REQUEST)
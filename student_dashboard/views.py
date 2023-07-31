from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from student_dashboard.serializers import StudentDashboardSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class StudentDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_classes = StudentDashboardSerializer


    def get (self, request):
        try:
            current_user = request.user

            user = User.objects.filter(email=current_user)

            if not user.exists():
                return Response({
                    'status': False,
                    'message': 'Student not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            user = user.first()


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
                    'message': 'Student portal account is suspended check in with IT...'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.serializer_classes(user)

            return Response({
                'status': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(str(e))
            return Response({
                'status': False,
                'message': 'Could not view dashboard data!'
            }, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()

from student_profile.serializers import StudentProfileSerializer

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

            })
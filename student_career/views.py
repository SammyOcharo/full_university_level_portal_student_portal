from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from student_career.models import Student
from student_career.serializers import ViewUnitsSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class ViewUnitsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewUnitsSerializer

    def get(self, request):
        try:
            current_user = request.user
            print("current_user: ", current_user)
            allowed_roles = ['admin']

            if not current_user.role.short_name in allowed_roles:
                return Response({
                    'status': False,
                    'message': f'role {current_user.role.short_name} not allowed to access this resource!'
                }, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.filter(email=current_user).first()
            student = Student.objects.filter(user=user)

            serializer = self.serializer_class(student)

            return Response({
                'status': True,
                'message': 'student units',
                'units': serializer.data
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Could not view student units'
            }, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import StudentLoginSerializer
# Create your views here.

class StudentLoginAPIView(APIView):
    serializer_class = StudentLoginSerializer

    def post(self, request):
        try:
            data = request.data

        except Exception as e:
            print(str(e))

            return Response({
                'status': False,
                'message': 'Error trying to login'
            }, status=status.HTTP_400_BAD_REQUEST)
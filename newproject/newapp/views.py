from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

class StudentApiView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return Response(serializer.data)
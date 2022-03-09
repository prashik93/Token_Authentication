from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permissions import IsReadOnly,IsGETorPUTorPOST
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

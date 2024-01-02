from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import Pagination
# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['passby','city']
    search_fields = ['^name']
    ordering_fields = ['name']
    
    
    pagination_class = Pagination

    # def get_queryset(self):
    #     golden_value = self.request.GET.get("golden")
    #     if golden_value:
    #         return Student.objects.filter(passby=golden_value)
    #     else:
    #         return Student.objects.all()
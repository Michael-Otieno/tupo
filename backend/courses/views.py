from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Course
from .serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'register':'register/',
        'login':'login/',
        
        
    }
    return Response(routes)


class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['description']
    pagination_class = PageNumberPagination
    parser_classes = (MultiPartParser, FormParser,FileUploadParser,)
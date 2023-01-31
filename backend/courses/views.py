from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Course
from .serializers import CourseSerializer,UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import generics
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'register':'register/',
        'login':'login/',
        
        
    }
    return Response(routes)


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['description']
    pagination_class = PageNumberPagination
    parser_classes = (MultiPartParser, FormParser,FileUploadParser,)

class CourseDetailView(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
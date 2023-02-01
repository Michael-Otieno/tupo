from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Course,User
from .serializers import CourseSerializer,UserSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = {
        '':'routes',
        'register':'register/',
        'login':'login/',
        'profile':'profile/',
        'changepassword':'changepassword/',
        'api-token':'api/token/',
        'api-token-refresh':'api/token/refresh'
        
        
    }
    return Response(routes)


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



# class LoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer
#     def post(self,request):
#         # email = request.data['email']
#         # password = request.data['password']
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')

#         # user = User.objects.get(email=email)
#         user = authenticate(email=email,password=password)
#         # print(user)
#         if user is None:
#             raise AuthenticationFailed('User not found')
#         # if user.check_password(password):
#         #     raise AuthenticationFailed('Incorrect password')
#         payload = {
#             'id':user.id,
#             'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat':datetime.datetime.utcnow() 
#         }
#         token = jwt.encode(payload,'secret',algorithm='HS256')
#         response = Response()
#         response.set_cookie(key='jwt',value=token,httponly=True)
#         response.data = {
#             'jwt':token
#         }
#         return response


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class ProfileView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ChangePasswordView(generics.GenericAPIView):
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'},status=status.HTTP_200_OK)


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
    
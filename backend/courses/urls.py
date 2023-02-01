from django.urls import path,include
from . import views
from .views import CourseView,CourseDetailView,RegisterView,LoginView,MyTokenObtainPairView,ProfileView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("",views.getRoutes),
    path("courses/",CourseView.as_view()),
    path("course/<int:pk>/",CourseDetailView.as_view()),
    path("register/",RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
from django.urls import path,include
from . import views
from .views import CourseView,CourseDetailView,RegisterView,LoginView

urlpatterns = [
    path("",views.getRoutes),
    path("courses/",CourseView.as_view()),
    path("course/<int:pk>/",CourseDetailView.as_view()),
    path("register/",RegisterView.as_view()),
    path('login/', LoginView.as_view()),

]
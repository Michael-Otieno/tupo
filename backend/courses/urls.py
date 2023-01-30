from django.urls import path,include
from . import views
from .views import CourseView,CourseDetailView

urlpatterns = [
    path("",views.getRoutes),
    path("courses/",CourseView.as_view()),
    path("course/<int:pk>/",CourseDetailView.as_view())

]
from django.urls import path,include
from . import views
from .views import CourseView

urlpatterns = [
    path("",views.getRoutes),
    path("courser/",CourseView.as_view())
]
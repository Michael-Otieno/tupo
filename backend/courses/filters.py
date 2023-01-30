from django_filters.rest_framework import FilterSet
from .models import Course

class CourseFilter(FilterSet):
  class Meta:
    model = Course
    fields = {
      'category':['exact'],
      'title':['exact']
    }
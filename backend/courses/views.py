from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'register':'register/',
        'login':'login/',
        
        
    }
    return Response(routes)
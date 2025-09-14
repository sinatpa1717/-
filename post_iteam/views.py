from django.shortcuts import render
from .models import My_model
from .serializers import seriall
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def page_api_web_post(request):
    post = My_model.objects.create()
    serial = seriall(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response (serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)


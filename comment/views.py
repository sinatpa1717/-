from django.shortcuts import render
from .serializers import comment_serial
from .models import comment_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def page_web_post_comment(request):
    model = comment_model.objects.create()
    serial = comment_serial(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response (serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

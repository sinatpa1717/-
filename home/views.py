from django.shortcuts import render  
from post_iteam.models import My_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from post_iteam.serializers import seriall

@api_view(['GET'])
def page_web_api_get(request):
    model = My_model.objects.all()
    serial = seriall(model, many = True)
    return Response (serial.data)

@api_view(['GET'])
def page_Web_api_up(request):
    model = My_model.objects.all().order_by('data')
    seria = seriall(model, many = True)
    return Response (seria.data)

@api_view(['GET'])
def page_Web_api_down(request):
    mdoel = My_model.objects.all().order_by("-data")
    serial  = seriall(mdoel, many = True)
    return Response (serial.data)

@api_view(['GET'])
def page_web_api_count(request):
    count = My_model.objects.count()
    return Response ({"count" : count})


@api_view(['GET'])
def page_web_api_search(request):
    q = request.GET.get("q")  
    if q:
        results = My_model.objects.filter(name__icontains=q) 
        serializer = seriall(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "پارامتر جستجو وارد نشده"}, status=status.HTTP_400_BAD_REQUEST)

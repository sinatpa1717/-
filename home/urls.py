from django.urls import path
from .views import page_web_api_get, page_web_api_search,page_web_api_count,page_Web_api_down,page_Web_api_up

urlpatterns = [
    path("api/get/home/", page_web_api_get),
    path("api/get/up/", page_Web_api_up),
    path("api/get/down/", page_Web_api_down),
    path("api/get/count/", page_web_api_count),
    path("api/get/search/", page_web_api_search)
    
]
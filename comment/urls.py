from django.urls import path
from .views import page_web_post_comment

urlpatterns = [
    path("" , page_web_post_comment),
]
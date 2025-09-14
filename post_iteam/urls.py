from django.urls import path
from .views import page_api_web_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , page_api_web_post)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


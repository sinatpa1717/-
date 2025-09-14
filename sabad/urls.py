from django.urls import path
from .views import sabad_kharid, remove_from_cart

urlpatterns = [
    path("sabad/<int:sabad_id>/", sabad_kharid, name="sabad_kharid"),
    path("sabad/<int:sabad_id>/remove/<int:pk>/", remove_from_cart, name="remove_from_cart"),
]
from rest_framework import serializers
from .models import comment_model

class comment_serial(serializers.Serializer):
    class Meta:
        model = comment_model
        fields = "__all__"
        
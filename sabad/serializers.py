from rest_framework import serializers
from .models import sabad , iteam , Iteam_sabad

class serial_sabad(serializers.ModelSerializer):
    class Meta:
        model = sabad
        fields = "__all__"
    
class serial_iteam(serializers.ModelSerializer):
    class Meta:
        model = iteam
        fields = "__all__"

class serial_iteam_sabad(serializers.ModelSerializer):
    class Meta:
        model = Iteam_sabad
        fields = "__all__"
        
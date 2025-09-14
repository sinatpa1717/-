from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import serial_iteam_sabad
from .models import Iteam_sabad


# گرفتن همه آیتم‌های یک سبد
@api_view(['GET'])
def sabad_kharid(request, sabad_id):
    model = Iteam_sabad.objects.filter(cart_id=sabad_id)   # فقط همون سبد
    serial = serial_iteam_sabad(model, many=True)
    return Response(serial.data)


# حذف یک آیتم از یک سبد خاص
@api_view(['DELETE'])
def remove_from_cart(request, sabad_id, pk):
    try:
        item = Iteam_sabad.objects.get(cart_id=sabad_id, id=pk)
        item.delete()
        return Response({"message": "Deleted"})
    except Iteam_sabad.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

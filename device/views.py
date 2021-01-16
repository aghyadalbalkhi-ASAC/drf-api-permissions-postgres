from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView , RetrieveUpdateDestroyAPIView

from .models import Device
from .serializer import DeviceSerializer
# Create your views here.


class DeviceGet(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceGetInfo(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
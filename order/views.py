from django.shortcuts import render
from order.serializers import *
from rest_framework import viewsets
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = Order
    queryset = Order.objects.all()
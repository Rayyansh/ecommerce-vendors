from django.shortcuts import render
from accounts.models import *
from accounts.serializers import *
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BannerImageViewset(viewsets.ModelViewSet):
    serializer_class = BannerImageSerializer
    queryset = BannerImage.objects.all()

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class SupportViewSet(viewsets.ModelViewSet):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()


class EnquiryViewSet(viewsets.ModelViewSet):
    serializer_class = EnquirySerializer
    queryset = Enquiry.objects.all()


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
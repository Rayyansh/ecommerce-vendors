from django.urls import path
from order.views import *

order = OrderViewSet.as_view({"get":"list","post":"create"})

urlpatterns = [
    path('order/', order, name='order'),
]
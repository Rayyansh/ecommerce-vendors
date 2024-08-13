from django.contrib import admin
from django.urls import path
from accounts.views import *

user = UserViewSet.as_view({'get':'list','post':'create'})
banner_image = BannerImageViewset.as_view({'get':'list','post':'create'})
transaction = TransactionViewSet.as_view({'get':'list','post':'create'})
support = SupportViewSet.as_view({'get':'list','post':'create'})
enquiry = EnquiryViewSet.as_view({'get': 'list', 'post': 'create'})
ticket = TicketViewSet.as_view({'get':'list','post':'create'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user, name='user'),
    path('banner-image/', banner_image, name='banner-image'),
    path('transaction/', transaction, name='transaction'),
    path('support/', support, name='support'),
    path('enquiry/', enquiry, name='enquiry'),
    path('ticket/', ticket, name='ticket'),
]
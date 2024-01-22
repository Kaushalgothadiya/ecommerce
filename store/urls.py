from django.urls import path
from .views import *

urlpatterns=[
    path('',my_view,name='my_view'),
    path('get-item-prices/<int:item_id>/',get_item_prices,name='get_item_price'),
    path('redirect_view/',redirect_view,name='redirect_view'),
    path('order/',get_order,name='get_order'),
    path('delete_order/<int:order_id>',delete_order,name='delete_order'),
]
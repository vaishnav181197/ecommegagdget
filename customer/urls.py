from django.urls import path
from .views import *


urlpatterns=[
    path('productdet/<int:id>',ProductDetailsView.as_view(),name="prodet"),
    path('addtocart/<int:id>',AddtoCartView.as_view(),name='acart'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('remcart/<int:id>',DeltecartItemView.as_view(),name="rcart"),
    path('cout/<int:id>',Checkoutview.as_view(),name='cout'),
    path('orders',OrderList.as_view(),name="order"),
    path('corder/<int:id>',cancelorder,name='corder'),
    path('addreview/<int:id>',addreview,name='areview')
]
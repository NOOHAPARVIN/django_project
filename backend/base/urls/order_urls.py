from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('<str:pk>/', views.getOrderById, name='user-order'),  # Ensure you have a trailing slash here
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]

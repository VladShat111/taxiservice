from django.urls import path

from .views import (OrdersView,
                    OrderDetailView,
                    register_page,
                    login_user, logout_user,
                    order_form_creation,
                    change_taxi_state)

urlpatterns = [
    path('orders/', OrdersView.as_view(), name='all_orders'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='one_order'),
    path('registration/', register_page, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/order/', order_form_creation, name='form_create'),
    path('delete_order/<int:pk>/', change_taxi_state, name='delete')
]

from django.urls import path
from . import views
from django.urls import reverse_lazy

app_name = 'subscription'

urlpatterns = [

    path('', views.index, name="home"),
    path('details/<int:id>', views.details, name="details"),
    path('payment', views.payment, name="payment"),
    path('checkout/', views.CheckoutSession.as_view(), name='checkout'),
    path('checkout-success/', views.CheckoutSuccess.as_view(),name='checkout_success'),
    path('checkout-cancel/', views.CheckoutCancel.as_view(), name='checkout_cancel'),

]
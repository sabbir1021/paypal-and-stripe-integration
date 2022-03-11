from django.urls import path
from . import views
from django.urls import reverse_lazy

app_name = 'subscription'

urlpatterns = [

    path('', views.index, name="home"),
    path('details/<int:id>', views.details, name="details"),
    path('payment', views.payment, name="payment"),

]
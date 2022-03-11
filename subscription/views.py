from django.shortcuts import render
from .models import Subscription, Payments
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def index(request):
    subscrip = Subscription.objects.all()
    return render(request, "index.html",{'subscrip':subscrip})


def details(request, id):
    subscrip = Subscription.objects.get(id=id)
    return render(request, "details.html",{'subscrip':subscrip})


def payment(request):
    body = json.loads(request.body)
    print("Body:",body)
    package = Subscription.objects.get(id=body["package_id"])
    payment_type = body["payment_type"]
    user = User.objects.get(id=body["user"])
    pay = Payments(subscription=package, payment_type=payment_type)
    pay.user = user
    pay.save()
    return JsonResponse('Payment completed!', safe=False)
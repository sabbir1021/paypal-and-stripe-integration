from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscription, Payments
from django.urls import reverse
import json
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

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


class CheckoutSession(View):
    def post(self, request, *args, **kwargs):
        package = Subscription.objects.get(id=request.POST['course'])
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'name': package.name,
                        'description': package.name,
                        'quantity': 1,
                        'currency': 'EUR',
                        'amount':  int(package.price * 100),
                       
                    }
                ],
                payment_method_types=[
                    'card',
                ],
                mode='payment',
                
                success_url=request.build_absolute_uri(
                    reverse('subscription:checkout_success')),
                cancel_url=request.build_absolute_uri(
                    reverse('subscription:checkout_cancel'))
            )
        except Exception as e:
            print(e)
            return str(e)
        return HttpResponseRedirect(checkout_session.url)


class CheckoutSuccess(TemplateView):
    template_name = "checkout_success.html"


class CheckoutCancel(TemplateView):
    template_name = "checkout_success.html"
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

PAYMENT_TYPE = (
    ("PAY", "PAYPAL"),
    ("STR", "STRIPS"),
)

class Subscription(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Payments(models.Model):
    subscription = models.ForeignKey(Subscription,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type =  models.CharField(max_length=3,choices=PAYMENT_TYPE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.username
# paymentapp/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_id} - {self.amount} {self.currency}"

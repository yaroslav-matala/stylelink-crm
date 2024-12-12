from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=300, blank=True)
    formula = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clients'
        )

    def __str__(self):
        return self.name

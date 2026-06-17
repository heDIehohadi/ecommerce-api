from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    ADMIN = "admin", "Admin"


class StoreUsers(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
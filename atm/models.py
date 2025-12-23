from django.db import models
from django.utils import timezone

class Account(models.Model):
    name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=20, unique=True)
    pin = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.card_number})"


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('Deposit', 'Deposit'),
        ('Withdraw', 'Withdraw'),
        ('Transfer', 'Transfer'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.account} | {self.type} | {self.amount}"

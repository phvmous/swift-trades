from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    cash_balance = models.DecimalField(max_digits=65, decimal_places=2, default=10000.00)

    def __str__(self):
        return self.name

class Stock(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=65, decimal_places=2)
    shares = models.IntegerField()

    def __str__(self):
        return self.name

class Trade(models.Model):
    TYPE = (
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    symbol = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=65, decimal_places=2)
    shares = models.IntegerField()
    order_type = models.CharField(max_length=10, choices=TYPE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Trade #' + str(self.id)
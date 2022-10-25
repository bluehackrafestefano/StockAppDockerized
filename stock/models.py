from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(UpdateCreate):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    stock = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class Firm(UpdateCreate):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Stock(UpdateCreate):
    TRANSACTION = (
        ('I', 'IN'),
        ('O', 'OUT')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(
        Firm, on_delete=models.SET_NULL, null=True, related_name='firm_stock')
    transaction = models.CharField(max_length=1, choices=TRANSACTION)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stocks')
    quantitiy = models.SmallIntegerField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    price_total = models.DecimalField(
        max_digits=9, decimal_places=2, validators=[MinValueValidator(1)], blank=True, null=True)

    def __str__(self):
        return f'{self.transaction} - {self.product} - {self.quantitiy}'

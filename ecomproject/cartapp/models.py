from django.db import models
from Ecomapp.models import Products


# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    adddate=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['adddate']

    def __str__(self):
        return '{}'.format(self.cid)

class Cartitem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cartitem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
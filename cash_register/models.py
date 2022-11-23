from django.db import models

class  Items(models.Model):
    itemCode = models.CharField(max_length=10)
    itemName = models.CharField(max_length=50)
    itemPrice = models.FloatField(default=0)
    
    class  Meta:
        verbose_name_plural = "Items"

class  Orders(models.Model):
    itemCode = models.CharField(max_length=100)
    itemName = models.CharField(max_length=50, default='Null')
    itemPrice = models.CharField(max_length=50, default='Null')
    totalPrice = models.FloatField(default=0)
    
    class  Meta:
        verbose_name_plural = "Orders"

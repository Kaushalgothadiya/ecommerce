from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

class Item(models.Model):
    item_name=models.CharField(max_length=50)
    item_price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    customer_name=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    total_price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"order-{self.id}"
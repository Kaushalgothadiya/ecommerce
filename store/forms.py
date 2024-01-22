from django import forms
from .models import Order,Customer,Item
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        # fields=['customer_name','item','price','quantity','total_price']
        fields='__all__'
    # customername=forms.(label="Name",max_length=50)
    # item=forms.CharField(label="item",max_length=50)
    # price=forms.DecimalField(label="price",max_digits=6,decimal_places=2)
    # quantity=forms.IntegerField(label="quantity")
    # totalprice=forms.DecimalField(label="totalprice",max_digits=10,decimal_places=2)
    customer_name=forms.ModelChoiceField(queryset=Customer.objects.all(),label="customer")
    item=forms.ModelChoiceField(queryset=Item.objects.all(),label="Item")
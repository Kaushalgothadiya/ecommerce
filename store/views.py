from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q

# Create your views here.
def my_view(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print('save successfully')
            return redirect('redirect_view')
    else:
        form=OrderForm()
    context={'form':form}

    return render(request,'store.html',context=context)

def redirect_view(request):
    return HttpResponse('success..')

def get_item_prices(request,item_id):
    try:
        
        item=Item.objects.get(id=item_id)
        data={'prices':item.item_price}
        print(data)
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse({'error':'Item not found'},status=404)

def get_order(request):

    if 'search' in request.GET:
        search_term=request.GET.get('search','')
        print(search_term)
        orders=Order.objects.filter(
            Q(item__item_name__icontains=search_term) |  
            Q(customer_name__first_name__icontains=search_term)
        )
    else:
        orders=Order.objects.all()
        search_term=''
    
    context={'orders':orders,'search_term':search_term}
    return render(request,'order.html',context)


# delete order:
def delete_order(request,order_id):
    orders=Order.objects.get(id=order_id)
    orders.delete()
    
    return redirect('get_order')

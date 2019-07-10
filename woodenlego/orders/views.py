from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'],user=request.user)
            cart.cart.clear()
            #order_created.delay(order.id)
            request.session['order_id'] = order.id
            #return render(request,'orders/created.html',{'order':order})
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()

    return render(request, 'orders/create.html', {'form': form})
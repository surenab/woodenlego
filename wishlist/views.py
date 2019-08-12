from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import WishItem
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
class WishesView(ListView):
    template_name = 'product_wishlist.html'
    context_object_name = 'wish_list'
    paginate_by = 10

    def get_queryset(self):
        return WishItem.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required(login_url='/accounts/login/')
def delete_wish(request,pk):
    wish = get_object_or_404(WishItem, product_id=pk)
    wish.delete()
    return redirect('wishes')

@login_required(login_url='/accounts/login/')
def add_wish(request,pk):
    wish = WishItem.objects.filter(product_id=pk)
    if len(wish) == 0:
        WishItem.objects.create(user_id=request.user.id,product_id=pk)
    return redirect('wishes')

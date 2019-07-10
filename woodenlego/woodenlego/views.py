from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from orders.models import OrderItem
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('wlwebsite:home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class OrdersView(ListView):
    template_name = 'orders.html'
    context_object_name = 'order_list'
    paginate_by = 10

    def get_queryset(self):
        curent_user = self.request.user
        return OrderItem.objects.filter(user=curent_user).order_by('-order__created')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


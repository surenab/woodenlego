from django.shortcuts import render
from .models import ToyReview, Toy, DeliveryCost
from django.views import generic
# Create your views here.
from django.views.generic.base import TemplateView
from random import choices
from cart.forms import CartAddProductForm

class Home(generic.ListView):
    template_name = 'index_1.html'
    context_object_name = 'detailed_data'
    model = Toy

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['toy_list'] = set(choices(population=Toy.objects.all(), k=4))
        context['toy_list_feature'] = set(choices(population=Toy.objects.all(), k=4))
        context['toy_list'] = Toy.objects.all()[:4]
        context['sale'] = Toy.objects.get(sale=True)
        context['sale_perc'] = (context['sale'].price-context['sale'].real_price)*100/context['sale'].price
        context['sale_perc'] = int(context['sale_perc'])
        context['toy_list_feature'] = Toy.objects.all()[:4]
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context


class About(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Terms(TemplateView):
    template_name = 'terms.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Privacy(TemplateView):
    template_name = 'privacy.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Delivery(TemplateView):
    template_name = 'delivery.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Owners(TemplateView):
    template_name = 'aboutowners.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Ideas(TemplateView):
    template_name = 'ideas.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class Feature(TemplateView):
    template_name = 'feature.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context


class Products(generic.ListView):
    template_name = 'product_1.html'
    context_object_name = 'product_list'
    paginate_by = 12
    def get_queryset(self):
        if 'sort_by' not in self.request.GET.keys():
            return Toy.objects.order_by('-adddate')
        else:
            return Toy.objects.order_by(self.request.GET['sort_by'])
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context


class Blogs(TemplateView):
    template_name = 'blog_3.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context
class Contactus(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context

class ToyDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'detailed_data'
    model = Toy
    cart_product_form = CartAddProductForm()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['toy_list'] = set(choices(population=Toy.objects.all(), k=4))
        context['review_list'] = ToyReview.objects.filter(toy_id=kwargs['object'].id)
        context['cart_product_form'] = self.cart_product_form
        context['delivery'] = DeliveryCost.objects.get(id=1)
        return context
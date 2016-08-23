from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
    template_name = 'catalog/product_list.html'
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, template_name, context)

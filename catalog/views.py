from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category


# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    # ou
    # queryset = Product.objects.all()
    template_name = 'catalog/product_list.html'
    # Aqui, a variáve de listagem do contexto é definida com context_object_name
    # Se não for informado, será o nome da classe + _list = product_list
    context_object_name = 'products'
    # Fazendo paginação da view
    paginate_by = 3


# def category(request, slug):
#     category = Category.objects.get(slug=slug)
#     template_name = 'catalog/category.html'
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category),
#     }
#     return render(request, template_name, context)
class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    # Fazendo paginação da view
    paginate_by = 3

    def get_queryset(self):
        # Esta seria a primeira forma de acessar os produtos da categoria que veio na URL
        # category = get_object_or_404(Category, slug=self.kwargs['slug'])
        # return Product.objects.filter(category=category)
        # A segunda forma seria fazer de forma direta
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


def product(request, slug):
    product = Product.objects.get(slug=slug)
    template_name = 'catalog/product.html'
    context = {
        'product': product
    }
    return render(request, template_name, context)


# Definições das views baseadas nas ClassBasedVIews
product_list = ProductListView.as_view()
category = CategoryListView.as_view()

from django.contrib import admin
# Minhas importações
from .models import Product, Category


# Classe para gerenciar o admin da aplicação, visualmente falando
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    # list_filter serão os campos que estarão disponíveis para realizar um filtro na barra lateral
    list_filter = ['created', 'modified']


# Classe para gerenciar o admin da aplicação, visualmente falando
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    # Um recurso interessante do admin, na parte de campos para pesquisa, é a possibilidade de
    # se fazer a pesquisa por um campo ForeignKey. Nesse caso, pelo nome da categoria do produto
    # É utilizado o formato de lookup do nome da categoria no formato category__name
    search_fields = ['name', 'slug', 'category__name']
    # list_filter serão os campos que estarão disponíveis para realizar um filtro na barra lateral
    list_filter = ['created', 'modified']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
    # Campos comuns
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    # Campos específicos
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def get_absolute_url(self):
        # Reverse possui tres parametros:
        # 1 - A URL nomeada
        # 2 - Os parametros não nomeados (args)
        # 3 - Os parametros nomeados (kwargs)
        return reverse('catalog:category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    # Campos comuns
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    # Campos específicos
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})

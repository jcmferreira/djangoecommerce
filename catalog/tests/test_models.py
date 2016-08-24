from django.test import TestCase
from django.core.urlresolvers import reverse
from catalog.models import Product
from model_mommy import mommy


class CategoryTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    # O método tearDow é executado sempre que um def é finalizado
    def tearDown(self):
        pass

    # Testando a URL absoluta
    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug})
        )


class ProductTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'produto'})
        )

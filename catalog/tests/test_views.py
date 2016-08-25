from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# from catalog.models import Product
from model_mommy import mommy


class ProductListTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)

    # O método tearDow é executado sempre que um def é finalizado
    def tearDown(self):
        for product in self.products:
            product.delete()

    # Testando a View ok
    def test_view_ok(self):
        response = self.client.get(self.url)
        # Testando se a página foi acessada corretamente , código 200
        self.assertEqual(response.status_code, 200)
        # Testando se o template usado está correto
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    # Validando o conteúdo do contexto
    def test_context(self):
        response = self.client.get(self.url)
        # Testando se a variável product_list existe no contexto
        self.assertTrue('products' in response.context)
        # Testando existem 10 produtos, assim como define a criação com o mommy.make
        product_list = response.context['products']
        self.assertEqual(product_list.count(), 3)
        # Como existe a paginação, ela tbm deve ser testada
        # No caso, como existem três produtos por página, para 10 produtos, serão 4 páginas
        paginator = response.context['paginator']
        self.assertEqual(paginator.num_pages, 4)

    # Validando página inválida
    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEqual(response.status_code, 404)

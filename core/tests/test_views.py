from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    # O método tearDow é executado sempre que um def é finalizado
    def tearDown(self):
        pass

    # Teste simples para verificar se o index do sistema está correto (código: 200)
    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    # Verificando se o template correto está sendo usado
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

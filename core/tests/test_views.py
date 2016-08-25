from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail


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


class ContactViewTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url, data)
        # assertFormError precisa do nome do form dentro do contexto
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_form_ok(self):
        data = {'name': 'nome', 'message': 'mensagem', 'email': 'test@test.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        # Aqui, é possível acessar mail.outbox (caixa de saída) e verificar se foi enviado o email
        self.assertEqual(len(mail.outbox), 1)
        # Aqui, é possível acessar mail.outbox (caixa de saída) e verificar o assunto do email enviado
        self.assertEqual(mail.outbox[0].subject, 'Assunto: Contato do Django e-Commerce')

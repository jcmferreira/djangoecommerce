from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from model_mommy import mommy

User = get_user_model()


class RegisterViewTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {
            'username': 'juliocesar',
            'password1': 'teste123456xeba',
            'password2': 'teste123456xeba',
            'email': 'test@test.com',
        }
        index_url = reverse('index')
        response = self.client.post(self.register_url, data)

        # Testando se foi redirecionado para a página inicial
        self.assertRedirects(response, index_url)
        # Validando se o usuário existe
        self.assertEqual(User.objects.count(), 1)

    def test_register_error(self):
        data = {
            'username': 'juliocesar',
            'password1': 'teste123456xeba',
            'password2': 'teste123456xeba'
        }
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    # Testando o login correto do usuário
    def test_update_user_ok(self):
        data = {
            'name': 'test',
            'email': 'test@test.com',
        }
        response = self.client.get(self.url)
        # Login com erro
        self.assertEqual(response.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        # Login ok
        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        # Validando os dados do login feito
        # O usuário pode ser recuperado de duas formas:
        # 1 - user = User.objects.get(username=self.user.username)
        # 2 - self.user.refresh_from_db()
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.name, 'test')

    # Testando o login errado
    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdatePasswordTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('teste123xeba')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {
            'old_password': '123',
            'new_password1': 'teste123xeba',
            'new_password2': 'teste123xeba',
        }
        self.client.login(username=self.user.username, password='teste123xeba')
        self.user.refresh_from_db
        self.client.post(self.url, data)
        self.assertTrue(self.user.check_password('teste123xeba'))

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


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

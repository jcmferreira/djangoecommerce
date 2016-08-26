from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
from django.conf import settings
from django.contrib.auth import get_user_model
from model_mommy import mommy


User = get_user_model()


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


class LoginViewTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        # O método prepare do Mommy cria o object mas não salva
        # A chamada settings.AUTH_USER_MODEL indica qual é o model de usuário que está sendo utilizado
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        # Foi feito sem salvar para podermos definir a senha
        self.user.set_password('123')
        # Salvando
        self.user.save()

    # O método tearDow é executado sempre que um def é finalizado
    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.url)

        # Confirmando se o usuário não está logado de verdade
        self.assertTrue(not response.wsgi_request.user.is_authenticated())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        data = {
            'username': self.user.username,
            'password': '123'
        }
        # Enviando os dados do usuário
        response = self.client.post(self.url, data)
        # URL de redirecionamento para o login que foi validado
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)
        # Confirmando se o usuário está logado de verdade
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_login_error(self):
        data = {
            'username': self.user.username,
            'password': '1234'
        }
        # Enviando os dados do usuário
        response = self.client.post(self.url, data)
        # Template ok
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        # Validação da senha errada. Esta é a mensagem exata que é gerada para senhas erradas
        error_msg = ('Por favor, entre com um usuário  e senha corretos.'
                     ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None, error_msg)


class RegisterViewTestCase(TestCase):
    # O método setUp é executado sempre que um def é iniciado
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_ok(self):
        data = {
            'username': 'juliocesar',
            'password1': 'teste123456xeba',
            'password2': 'teste123456xeba'
        }
        index_url = reverse('index')
        response = self.client.post(self.register_url, data)
        # Testando se foi redirecionado para a página inicial
        self.assertRedirects(response, index_url)
        # Validando se o usuário existe
        self.assertEqual(User.objects.count(), 1)

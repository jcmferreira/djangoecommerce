# from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
# O import login_required é usado se a view é baseada em função (def)
# O import LoginRequiredMixin é usado se a view é baseada em classe (nosso caso)
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Form padrão do django para fazer a alteração de senha automaticamente
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from .forms import UserAdminCreationForm


# Create your views here.
# Aqui, basta herdar a nossa view de LoginRequiredMixin para que o controle de login passe a funcionar
# Para funcionar, é preciso que o LoginRequiredMixin seja a primeira classe
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    # Definição dos campos que poderão ser atualizados
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    # Por padrão, o método get_object da classe pai procura por um slug ou id na URL.
    # Aqui, estamos dizendo que o usuário é a própria instância de User de quem está logado
    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    # Método para gerar os argumentos que serão passados para o formulário do Django
    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        # Adicionando o nosso user para o formulário do Django
        kwargs['user'] = self.request.user
        return kwargs

    # Para fazer valer o formulário de login, os dados precisam ser salvos (visto no teste de login)
    # Nesse caso, é sobrescrita a chamada de form_valid para salvar os dados do formulário antes de retorná-lo
    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


# Definição das variáveis para as views criadas
index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()

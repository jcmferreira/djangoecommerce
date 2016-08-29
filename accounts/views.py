# from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.urlresolvers import reverse_lazy
# O import login_required é usado se a view é baseada em função (def)
# O import LoginRequiredMixin é usado se a view é baseada em classe (nosso caso)
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


class UpdateUserView(UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    # Definição dos campos que poderão ser atualizados
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    # Por padrão, o método get_object da classe pai procura por um slug ou id na URL.
    # Aqui, estamos dizendo que o usuário é a própria instância de User de quem está logado
    def get_object(self, queryset=None):
        return self.request.user


# Definição das variáveis para as views criadas
index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()

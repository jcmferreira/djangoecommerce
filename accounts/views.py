# from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
# O import login_required é usado se a view é baseada em função (def)
# O import LoginRequiredMixin é usado se a view é baseada em classe (nosso caso)
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserAdminCreationForm


# Create your views here.
# Aqui, basta herdar a nossa view de LoginRequiredMixin para que o controle de login passe a funcionar
# Para funcionar, é preciso que o LoginRequiredMixin seja o primeiro na listagem de herança
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


# Definindo a view RegisterView para a variável usada na URL
index = IndexView.as_view()
register = RegisterView.as_view()

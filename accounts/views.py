# from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm


# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


# Definindo a view RegisterView para a variável usada na URL
register = RegisterView.as_view()

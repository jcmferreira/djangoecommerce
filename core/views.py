from django.shortcuts import render
from django.views.generic import TemplateView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse_lazy
# Views padrões do Django
from .forms import ContactForm


# Definindo a classe User padrão
User = get_user_model()


# Opção 1
# View principal do sistema
# def index(request):
#    template_name = 'index.html'
#    return render(request, template_name)


# Opção 2
# Aqui, a view index foi substituida por uma classe IndexView, com o método __call__
# Isso vai fazer com que a classe possa ser "chamável" pelo Django
# class IndexView(object):
#     def __call__(self, request):
#         return render(request, 'index.html')
#
# index é uma instancia de IndexView. Mas como a classe IndexView tem o método __call__,
# a variável index passa a pode ser chamável
# index = IndexView()


# Opção 3
# A classe acima foi reescrita usando a view-mãe do Django, a View. Agora, o método __call__ deixa de ser
# implementado e passamos a implementar o método get
# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')


# Opção 4
# Utilizando o TemplateView
class IndexView(TemplateView):
    template_name = 'index.html'


def contact(request):
    template_name = 'contact.html'
    success = False

    # Instanciando o formulário e validando se ele deverá ser vazio(sem erros = None)
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        from django.contrib import messages
        messages.error(request, 'Formulário inválido')

    context = {
        'form': form,
        'success': success
    }
    return render(request, template_name, context)


# Criando os objetos views para as URLs utilizarem
index = IndexView.as_view()

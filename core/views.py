from django.shortcuts import render
from .forms import ContactForm
# Views padrões do Django
from django.views.generic import View, TemplateView


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

# Como a classe IndexView passou a herdar de View, a chamada precisa usar o método as_view()
index = IndexView.as_view()


def contact(request):
    template_name = 'contact.html'
    success = False

    # Instanciando o formulário e validando se ele deverá ser vazio(sem erros = None)
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        success = True

    context = {
        'form': form,
        'success': success
    }
    return render(request, template_name, context)

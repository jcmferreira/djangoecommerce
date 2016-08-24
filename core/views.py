from django.shortcuts import render
from .forms import ContactForm


# View principal do sistema
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


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

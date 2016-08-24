from django.shortcuts import render
from .forms import ContactForm


# View principal do sistema
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def contact(request):
    template_name = 'contact.html'
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, template_name, context)

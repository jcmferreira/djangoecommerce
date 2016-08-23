from django.shortcuts import render
# from django.http import HttpResponse


# View principal do sistema
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


def product(request):
    template_name = 'product.html'
    return render(request, template_name)

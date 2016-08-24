from django import forms


# Classe para definição dos campos do formulário de contatos
# Após criado, o formulário pode ser "renderizado" como:
# 1 - <p> = as_p()
# 2 - <table> = as_table()
class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # Aqui, é feita uma sobrecarga do def __init__ padrão
    # Este formato funciona mas não é elegante.
    # Para esse recurso, será usado o plugin django-widget-tweaks
    # Para tal, o widget-tweaks deverá ser adicionada aos apps instalados do settings
    # def __init__(self, *args, **kwargs):
    #     # Aqui, é executado o métod super (pai) com os parâmetros informados
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     # Aqui, é possível definir qual será a classe que o Django irá utilizar para renderizar os campos
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'

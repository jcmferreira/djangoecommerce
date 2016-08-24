from django import forms


# Classe para definição dos campos do formulário de contatos
# Após criado, o formulário pode ser "renderizado" como:
# 1 - <p> = as_p()
# 2 - <table> = as_table()
class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

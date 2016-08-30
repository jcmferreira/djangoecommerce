from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse_lazy

from .models import CartItem
from catalog.models import Product


# Create your views here.
class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # Tentando recuperar o produto
        product = get_object_or_404(Product, slug=self.kwargs['slug'])

        # Validando a sessão ativa
        if self.request.session.session_key is None:
            self.request.session.save()

        # Adicionando o produto (ou incrementando) no carrinho
        cart_item, created = CartItem.objects.add_item(self.request.session.session_key, product)

        # Alertando o usuário
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso!')
        else:
            messages.success(self.request, 'Produto foi atualizado no carrinho com sucesso!')

        # Redirecionando o usuário para o carrinho
        return reverse_lazy('checkout:cart_item')


class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(CartItem, fields=['quantity'], can_delete=True, extra=0)
        session_key = self.request.session.session_key

        # Aqui, é validada a sessão do usuário. Se sim, é pq ele já fez algo e o carrinho dele será buscado
        # Se não existir, será criado um CartItem.objects.none(), que nada mais é que uma queryset vazia
        if session_key:
            if clear:
                formset = CartItemFormSet(queryset=CartItem.objects.filter(cart_key=session_key))
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    # Esse método é sobrescrito sempre que se deseja modificar o contexto do template, adicionando ou modificando os
    # valores que serão disponibilizados no template durante o render da view
    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    # Método para realizar o post do carrinho
    # Métodos disponíveis: get, post, put, delete. Todos de acordo com o method definido no formulário HTML
    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        # Aqui, é realizado o padrão do método post, recuperando o contexto e renderizando o response com os kwargs
        context = self.get_context_data(**kwargs)
        # Se o formulário estiver válido, ele deverá ser salvo e o parâmetro clear irá como True
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso!')
            context['formset'] = self.get_formset(clear=True)
        # Aqui, sempre deve ser retornado o render_to_response. Ela usa o conteúdo de template_name e usa o context
        return self.render_to_response(context)

# Definindo a variável da view para uso nas URLs
create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()

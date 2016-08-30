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

    # Esse método é sobrescrito sempre que se deseja modificar o contexto do template, adicionando ou modificando os
    # valores que serão disponibilizados no template durante o render da view
    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        CartItemFormSet = modelformset_factory(CartItem, fields=['quantity'], can_delete=True, extra=0)

        # Aqui, é validada a sessão do usuário. Se sim, é pq ele já fez algo e o carrinho dele será buscado
        # Se não existir, será criado um CartItem.objects.none(), que nada mais é que uma queryset vazia
        session_key = self.request.session.session_key
        if session_key:
            context['formset'] = CartItemFormSet(queryset=CartItem.objects.filter(cart_key=session_key))
        else:
            context['formset'] = CartItemFormSet(queryset=CartItem.objects.none())

        return context

# Definindo a variável da view para uso nas URLs
create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()

from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.contrib import messages

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
        return product.get_absolute_url()


create_cartitem = CreateCartItemView.as_view()

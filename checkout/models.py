from django.db import models


# Create your models here.
class CartItemManager(models.Manager):
    # Validando a existência do item no carrinho:
    # 1. Se não existir, adiciona
    # 2. Se existir, incrementa a sua quantidade
    def add_item(self, cart_key, product):
        # Se o produto existe no carrinho, ele é retornado
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price)

        return cart_item, created


class CartItem(models.Model):
    # Para informar que o item de carrinho está ligado à outro item de carrinho
    # Esse campo irá utilizar o session_key, que possui o tamanho máximo de 40
    # A propriedade db_index=True irá criar um índice para o campo no banco de dados
    cart_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    # Demais campos do modelo
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    # Definindo o manager padrão do django com o nosso manager customizado
    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        # Definindo os campos que serão chave-composta única
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)


# Esta definição servirá para remover itens de carrinho que estejam com a quantidade zerada = 0 através de signals
def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

# O sinal para o django atualizar o carrinho através do def post_save_cart_item
# A definição do parâmetro sender=CartItem serve para dizer ao django que a função somente deverá ser disparada
# se quem chamou foi uma instância de CartItem
# dispatch_uid serve para garantir que a função será chamada uma única vez. É um registro dela. Um nome único
models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')

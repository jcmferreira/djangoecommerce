from django.db import models


# Create your models here.
class CartItem(models.Model):
    # Para informar que o item de carrinho está ligado à outro item de carrinho
    # Esse campo irá utilizar o session_key, que possui o tamanho máximo de 40
    # A propriedade db_index=True irá criar um índice para o campo no banco de dados
    cart_id = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    # Demais campos do modelo
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)

from .models import CartItem


# Um middleware é usado para intercalar uma chamada padrão no Django. Ou seja, é possível capturar o response
# e realizar tratamentos antes e depois do caminho padrão realizado pelo djangoself.
# Nesse caso abaixo, impementamos um middleware para capturar o get_response e podermos tratar o session_key
def cart_item_middleware(get_response):
    def middleware(request):
        # Capturando o session_key antes da requisição
        session_key = request.session.session_key
        # Executando a requisição
        response = get_response(request)
        # Tratando o session_key antes e após a requisição: se houve mudança, o carrinho com o session_key antigo
        # será atualizado para ter o novo session_key
        if session_key != request.session.session_key:
            CartItem.objects.filter(cart_key=session_key).update(cart_key=request.session.session_key)
        return response
    return middleware

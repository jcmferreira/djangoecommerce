from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model


# Aqui, é sobrescrita a classe ModelBackend, para realizarmos a autenticação de nosso sistema de usuários
# de uma forma diferente, mas que seja dentro do padrão do User do django, mesmo quando o User seja o nosso
# User customizado
class ModelBackend(BaseModelBackend):
    def authenticate(self, username=None, password=None):
        if username is not None:
            # Recuperando o modelo usuário
            UserModel = get_user_model()
            try:

                # Primeiro, tento achar o usuário pelo email, passando o parâmetro username
                user = UserModel.objects.get(email=username)

                # Se achou e a senha está correta, ele é retornado
                if user.check_password(password):
                    return user

            except UserModel.DoesNotExist:
                pass

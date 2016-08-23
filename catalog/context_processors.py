from .models import Category


# O arquivo context_processors irá servir para definir um padrão de contexto que deverá ser usado em
# qualquer view do projeto.
# No exemplo abaixo, criados um processor categories, que irá retornar as categorias cadastradas
# Este mesmo processor criado deverá ser adicionado ao context_processors do settings
def categories(request):
    return {
        'categories': Category.objects.all()
    }

from django.conf.urls import url
# A condição from . significa = do módulo atual
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
]

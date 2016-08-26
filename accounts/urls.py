from django.conf.urls import url
# A condição from . significa = do módulo atual
from . import views

urlpatterns = [
    url(r'^registro/$', views.register, name='register'),
]

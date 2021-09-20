from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TipoRegraViewSet, RegraEmailViewSet

routerEmail = SimpleRouter()
routerEmail.register('tipo_regra', TipoRegraViewSet)
routerEmail.register('regraemail', RegraEmailViewSet)

from rest_framework.routers import SimpleRouter

from administrativo.views import EntidadeViewSet, DiretoriaViewSet

routerAdministrativo = SimpleRouter()
routerAdministrativo.register('entidade', EntidadeViewSet)
routerAdministrativo.register('diretoria', DiretoriaViewSet)
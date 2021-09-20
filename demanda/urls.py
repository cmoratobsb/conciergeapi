from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import DocumentoViewSet, HistoricoDocumentoViewSet

routerDemanda = SimpleRouter()
routerDemanda.register('documentos', DocumentoViewSet)
routerDemanda.register('historicosdocumento', HistoricoDocumentoViewSet)

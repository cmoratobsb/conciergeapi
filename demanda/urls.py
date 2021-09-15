from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ( ListaDemandas,
                     DocumentoAPIView,
                     HistoricoDocumentoAPIView,
                     DocumentosAPIView,
                     HistoricosDocumentoAPIView,
                     DocumentoViewSet,
                     HistoricoDocumentoViewSet)
routerDemanda = SimpleRouter()
routerDemanda.register('documentos', DocumentoViewSet)
routerDemanda.register('historicosdocumento', HistoricoDocumentoViewSet)

urlpatterns = [
    path('todos_documentos', ListaDemandas.as_view(), name='index'),
    path('documentos/', DocumentosAPIView.as_view(), name='documentos'),
    path('historicodocumentos/', HistoricosDocumentoAPIView.as_view(), name='historicosdocumento'),
    path('documentos/<int:pk>/', DocumentoAPIView.as_view(), name='documentos'),
    path('historicodocumentos/<int:pk>/', HistoricoDocumentoAPIView.as_view(), name='historicosdocumento'),
   ]

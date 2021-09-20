from django.urls import path, include

from .views import IndexView, CreateDocumentoView, UpdateDocumentoView, DeleteDocumentoView, ListPontoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_documento/', CreateDocumentoView.as_view(), name='add_documento'),
    path('<int:pk>/update/', UpdateDocumentoView.as_view(), name='upd_documento'),
    path('<int:pk>/delete/', DeleteDocumentoView.as_view(), name='del_documento'),
    path('pontos/', ListPontoView.as_view(), name='pontos'),
]

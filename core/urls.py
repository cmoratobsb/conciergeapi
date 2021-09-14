from django.urls import path, include

from .views import IndexView, CreateDocumentoView, UpdateDocumentoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_documento/', CreateDocumentoView.as_view(), name='documento_form'),
    path('<int:pk>/update/', UpdateDocumentoView.as_view(), name='upd_documento'),
]

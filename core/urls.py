from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import IndexView, CreateDocumentoView, UpdateDocumentoView, DeleteDocumentoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_documento/', CreateDocumentoView.as_view(), name='add_documento'),
    path('<int:pk>/update/', UpdateDocumentoView.as_view(), name='upd_documento'),
    path('<int:pk>/delete/', DeleteDocumentoView.as_view(), name='del_documento'),
]

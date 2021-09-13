from rest_framework import viewsets

from .models import Entidade, Diretoria
from .serialaizers import EntidadeSerializer, DiretoriaSerializer


class EntidadeViewSet(viewsets.ModelViewSet):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer


class DiretoriaViewSet(viewsets.ModelViewSet):
    queryset = Diretoria.objects.all()
    serializer_class = DiretoriaSerializer

from rest_framework import viewsets

from .models import Tipo_Regra, Regra_Email
from .serialaizers import TipoRegraSerializer, RegraEmailSerializer


class TipoRegraViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Regra.objects.all()
    serializer_class = TipoRegraSerializer


class RegraEmailViewSet(viewsets.ModelViewSet):
    queryset = Regra_Email.objects.all()
    serializer_class = RegraEmailSerializer

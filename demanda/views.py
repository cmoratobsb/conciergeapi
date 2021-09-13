from django.views import generic
from rest_framework import generics
from rest_framework import viewsets

from .models import Documento, Historico_Documento
from .serialaizers import DocumentoSerializer, HistoricoDocumentoSerializer


class ListaDemandas(generic.ListView):
    model = Documento
    context_object_name = 'demanda'
    queryset = Documento.objects.order_by('?').all()
    template_name = 'listaDemandas.html'


class DocumentosAPIView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class DocumentoAPIView(generics.RetrieveDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class HistoricosDocumentoAPIView(generics.ListCreateAPIView):
    queryset = Historico_Documento.objects.all()
    serializer_class = HistoricoDocumentoSerializer


class HistoricoDocumentoAPIView(generics.RetrieveDestroyAPIView):
    queryset = Historico_Documento.objects.all()
    serializer_class = HistoricoDocumentoSerializer


'''
API V1
'''

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class HistoricoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = Historico_Documento.objects.all()
    serializer_class = HistoricoDocumentoSerializer

# class DocumentoAPIView(APIView):
#     def get(self, request):
#         documentos = Documento.objects.all()
#         serializer = DocumentoSerializer(documentos, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = DocumentoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class HistoricoDocumentoAPIView(APIView):
#     def get(self, request):
#         Historico_Documentos = Historico_Documento.objects.all()
#         serializer = HistoricoDocumentoSerializer(Historico_Documentos, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = HistoricoDocumentoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

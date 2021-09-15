from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import DocumentoForm

from demanda.models import Documento


class IndexView(ListView):
    model = Documento
    template_name = 'index.html'
    queryset = Documento.objects.order_by('id').all()
    context_object_name = 'documentos'


class CreateDocumentoView(CreateView):
    model = Documento
    template_name = 'documento_form.html'
    fields = ['id',
              'diretoria',
              # 'tipo_documento',
              # 'historico_documento',
              'titulo_documento',
              'tipo_documento',
              'situacao',
              'responsavel',
              'dat_ini',
              'dat_fim',
              'ativo']

    success_url = reverse_lazy('index')


class UpdateDocumentoView(UpdateView):
    model = Documento
    template_name = 'documento_form.html'
    fields = ['id',
              'diretoria',
              # 'tipo_documento',
              # 'historico_documento',
              'titulo_documento',
              'tipo_documento',
              'situacao',
              'responsavel',
              'dat_ini',
              'dat_fim',
              'ativo']
    success_url = reverse_lazy('index')


class DeleteDocumentoView(DeleteView):
    model = Documento
    template_name = 'documento_del.html'
    success_url = reverse_lazy('index')

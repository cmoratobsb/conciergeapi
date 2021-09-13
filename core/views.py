from django.views.generic import TemplateView

from demanda.models import Documento


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['documentos'] = Documento.objects.all()
        return context

from django import forms
from demanda.models import Documento


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = '__all__'


# class ContatoForm(forms.Form):
#     nome = forms.CharField(label='Nome', max_length=100)
#     email = forms.EmailField(label='E-mail', max_length=100)
#     assunto = forms.CharField(label='Assunto', max_length=100)
#     mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
#
#     def send_mail(self):
#         nome = self.cleaned_data['nome']
#         email = self.cleaned_data['email']
#         assunto = self.cleaned_data['assunto']
#         mensagem = self.cleaned_data['mensagem']
#
#         conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
#
#         mail = EmailMessage(
#             subject=assunto,
#             body=conteudo,
#             from_email='carlos.morato@gmail.com',
#             to=['carlos.morato@gmail.com', ],
#             headers={'Reply-To': email}
#         )
#         mail.send()




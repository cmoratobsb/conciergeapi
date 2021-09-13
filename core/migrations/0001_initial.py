# Generated by Django 3.2.6 on 2021-09-11 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda_Auditorias',
            fields=[
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição da Agenda')),
                ('dat_ini', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('dat_fim', models.DateField(blank=True, null=True, verbose_name='Data de Fim')),
                ('situacao', models.ForeignKey(on_delete=django.db.models.enums.Choices, to='administrativo.situacao')),
            ],
            options={
                'verbose_name': 'Agenda de Auditoria',
                'verbose_name_plural': 'Agendas de Auditoria',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255, verbose_name='Tipo de Documento')),
                ('descricao', models.TextField(blank=True, max_length=1000, null=True)),
                ('Origem_Documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.origem_documento')),
                ('agenda_auditoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.agenda_auditorias')),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.contato', verbose_name='Contato')),
                ('usu_petros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo de Controle',
                'verbose_name_plural': 'Tipos de Controle',
            },
        ),
    ]

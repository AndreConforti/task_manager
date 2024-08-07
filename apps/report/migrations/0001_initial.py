# Generated by Django 5.0.7 on 2024-08-05 01:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(blank=True, max_length=10, null=True)),
                ('subject', models.CharField(choices=[('analise_divergencia', 'Análise de Divergência'), ('quebra_coleta', 'Quebra de Coleta'), ('troca_erp', 'Troca de ERP'), ('troca_metodo', 'Troca de Método'), ('exclusao_dados', 'Exclusão de Dados')], max_length=30)),
                ('objective', models.CharField(choices=[('manutencao', 'Manutenção'), ('integração', 'Integração'), ('reintegração', 'Reintegração')], max_length=15)),
                ('integration_type', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('method', models.CharField(choices=[('ws_passivo', 'WS Passivo'), ('ws_ativo', 'WS Ativo'), ('email', 'E-mail'), ('publisher', 'Publisher'), ('ftp', 'FTP'), ('bd_remoto_view', 'Banco de Dados Remoto (View)'), ('bd_remoto_full', 'Banco de Dados Remoto Completo'), ('webcrawler', 'Webcrawler')], max_length=20)),
                ('validation_report', models.CharField(max_length=100)),
                ('activation_status', models.BooleanField(default=True)),
                ('validation', models.BooleanField(default=False)),
                ('task', models.BooleanField()),
                ('considerations', models.TextField()),
                ('action_required', models.CharField(blank=True, max_length=255)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('sales_manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='report.salesmanager')),
            ],
        ),
    ]

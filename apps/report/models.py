from django.db import models
from django.contrib.auth.models import User


class SalesManager(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Report(models.Model):
    OPTIONS_SUBJECT = (
        ('analise_divergencia', 'Análise de Divergência'),
        ('quebra_coleta', 'Quebra de Coleta'),
        ('troca_erp', 'Troca de ERP'),
        ('troca_metodo', 'Troca de Método'),
        ('exclusao_dados', 'Exclusão de Dados'),
    )
    OPTIONS_OBJECTIVE = (
        ('manutencao', 'Manutenção'),
        ('integração', 'Integração'),
        ('reintegração', 'Reintegração'),
    )
    OPTIONS_INTEGRATION = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    OPTIONS_METHOD = (
        ('ws_passivo', 'WS Passivo'),
        ('ws_ativo', 'WS Ativo'),
        ('email', 'E-mail'),
        ('publisher', 'Publisher'),
        ('ftp', 'FTP'),
        ('bd_remoto_view', 'Banco de Dados Remoto (View)'),
        ('bd_remoto_full', 'Banco de Dados Remoto Completo'),
        ('webcrawler', 'Webcrawler')
    )
    ticket = models.CharField(max_length=10, blank=True, null=True)
    subject = models.CharField(max_length=30, choices=OPTIONS_SUBJECT)
    objective = models.CharField(max_length=15, choices=OPTIONS_OBJECTIVE)
    responsible = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='user')
    integration_type = models.CharField(max_length=1, choices=OPTIONS_INTEGRATION)
    method = models.CharField(max_length=20, choices=OPTIONS_METHOD)
    validation_report = models.CharField(max_length=100)
    activation_status = models.BooleanField(default=True)
    validation = models.BooleanField(default=False)
    task = models.BooleanField()
    considerations = models.TextField()
    action_required = models.CharField(max_length=255, blank=True)
    sales_manager = models.ForeignKey(to=SalesManager, on_delete=models.DO_NOTHING)
    date_response = models.DateTimeField(auto_now=True)
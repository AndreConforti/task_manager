# Generated by Django 5.0.7 on 2024-08-16 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_report_validation_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='objective',
            field=models.CharField(choices=[('manutencao', 'Manutenção'), ('integração', 'Integração'), ('reintegração', 'Reintegração'), ('fechamento', 'Fechamento'), ('inapta', 'Unidade Inapta')], max_length=15),
        ),
        migrations.AlterField(
            model_name='report',
            name='subject',
            field=models.CharField(choices=[('analise_divergencia', 'Análise de Divergência'), ('quebra_coleta', 'Quebra de Coleta'), ('troca_erp', 'Troca de ERP'), ('troca_metodo', 'Troca de Método'), ('exclusao_dados', 'Exclusão de Dados'), ('pausa_atividades', 'Solicitação de Pausa nas Atividades')], max_length=30),
        ),
    ]
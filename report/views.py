from django.shortcuts import render
from django.http import HttpResponse

def etl(request):
    return HttpResponse('VOCÊ ENTROU EM BOLETIM ETL')
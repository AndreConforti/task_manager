## Determina a base do container
FROM python:3.10

## Atualizações
RUN apt-get update && apt-get upgrade -y

## Variável de ambiente / Com valor 1 determina que qualquer coisa q precisar ser exibida, vai ser exibida no terminal
ENV PYTHONUNBEFFERED 1

## Diretório onde vai ficar a aplicação dentro do container
WORKDIR /app/project

## Criação e ativação do ambiente virtual
RUN python -m venv .venv
RUN . .venv/bin/activate

## Copia o requirements
COPY requirements.txt ./

## Instala todas as dependências do projeto
RUN pip install -r requirements.txt

## Copia tudo pra dentro da pasta raiz
COPY . ./

## Determina a porta que vai rodar a aplicação
EXPOSE 8000

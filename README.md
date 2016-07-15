CatracaDigital
==============
[![Build Status](https://travis-ci.org/HeaTSolutions/CatracaDigital.svg?branch=master)](https://travis-ci.org/HeaTSolutions/CatracaDigital)
[![Code Health](https://landscape.io/github/HeaTSolutions/CatracaDigital/master/landscape.svg?style=flat)](https://landscape.io/github/HeaTSolutions/CatracaDigital/master)
[![codecov.io](https://codecov.io/github/HeaTSolutions/CatracaDigital/coverage.svg?branch=master)](https://codecov.io/github/HeaTSolutions/CatracaDigital?branch=master)

Solução para controle de ponto.

* O site pode ser acessado [aqui](http://www.catracadigital.com.br/).

Ambiente
========

Este projeto foi testado e desenvolvido com:
* Python 3.5.1
* Django 1.9.6

Instalação
==========

Pegue o código do repositório da seguinte maneira:

    git clone git@github.com:HeatSolutions/CatracaDigital.git

Copie o arquivo contrib/env-sample para o root do projeto com o nome .env:

    cp contrib/env-sample .env

Instale as dependências necessárias:

    pip install -r requirements/dev.txt

Migre as atualizações para o banco de dados:

    python manage.py migrate

Adicione as dependências de CSS no projeto:

    python manage.py bower install

Crie um usuário admin para ter acesso:

    python manage.py createsuperuser

Lance o servidor Django:

    python manage.py runserver

Testes
======

Os testes do CardDig foram implementados usando o
[framework de testes do Django](https://docs.djangoproject.com/en/1.9/topics/testing/overview/).

Para a execução dos testes:

    python manage.py test

Problemas conhecidos
====================

Nenhum problema reportado até então.

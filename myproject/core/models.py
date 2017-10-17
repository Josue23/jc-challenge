# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Candidate(User):
    phone = models.CharField('telefone', max_length=15)

    class Meta:
        verbose_name = 'candidato'
        verbose_name_plural = 'candidatos'

    def __unicode__(self):
    	return ' '.join([
            self.first_name,
            self.last_name,
        	])


class Empresa(models.Model):
    name = models.CharField('Empresa', max_length=100, unique=True)
    description = models.TextField('Descrição')
    

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']

    def __unicode__(self):
        return self.name


# empresa cria a vaga
class Vaga(models.Model):

    name = models.CharField('Nome da Vaga', max_length=100,  unique=True)
    empresa = models.ForeignKey('core.Empresa', verbose_name='Empresa')
    min_salario = models.DecimalField('Pretensão Mínima', decimal_places=2, max_digits=8,)
    max_salario = models.DecimalField('Pretensão Máxima', decimal_places=2, max_digits=8)
    experiencia = models.TextField('Experiência', max_length=150, default='Experiências profissionais')
    escolaridade = models.CharField('Escolaridade do candidato', max_length=100, blank=True)
    distancia = models.CharField('Distância máxima entre casa e trabalho', max_length=100, blank=True)


    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['name']

    def __unicode__(self):
        return self.name


# candidato escolhe a vaga
class CandidateChoice(models.Model):
    name = models.ForeignKey('core.Vaga', verbose_name='Escolha')
    min_salario = models.DecimalField('Pretensão Mínima', decimal_places=2, max_digits=8,)
    max_salario = models.DecimalField('Pretensão Máxima', decimal_places=2, max_digits=8)
    experiencia = models.TextField('Experiência', max_length=150)
    escolaridade = models.CharField('Escolaridade do candidato', max_length=100)
    distancia = models.CharField('Distância máxima entre casa e trabalho', max_length=100,)


    class Meta:
        verbose_name = 'Escolha'
        verbose_name_plural = 'Escolhas'
        ordering = ['name']

    def __unicode__(self):
        return self.name
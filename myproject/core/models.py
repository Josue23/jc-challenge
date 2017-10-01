from django.db import models
from django.contrib.auth.models import User


class Candidate(User):
    phone = models.CharField('telefone', max_length=50)

    class Meta:
        verbose_name = 'candidato'
        verbose_name_plural = 'candidatos'

    def __str__(self):
        return self.first_name
        return self.last_name

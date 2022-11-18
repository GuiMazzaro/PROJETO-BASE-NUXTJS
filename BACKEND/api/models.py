from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class NomeTabela(models.Model):
    atributoUm = models.CharField(max_length=100)
    atributoDois = models.CharField(max_length=100)

    def __str__(self):
        return self.atributoUm
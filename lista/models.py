


from typing import Any
from django.db import models

class Produtos(models.Model):
    produto = models.CharField(max_length=100, null=False,blank=False)
    preco = models.FloatField()

    def __str__(self):
        return self.produto
       
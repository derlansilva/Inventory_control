from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from product.models import Product

# Create your models here.

MOVEMENT = (
    ('e' , 'entrada'),
    ('s' , 'saida'),
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User , on_delete=models.CASCADE)
    nf = models.PositiveBigIntegerField('nota fiscal' , null = True , blank= True)
    movimento = models.CharField(max_length=1 , choices=MOVEMENT)

    class Meta:
        ordering  =('-created',)

    def __str__(self):
        return str(self.pk)


class EstoqueItens(models.Model):
    estoque =models.ForeignKey( Estoque , on_delete= models.CASCADE)
    produto = models.ForeignKey(Product ,  on_delete=models.CASCADE)
    quantidade= models.PositiveBigIntegerField()
    saldo= models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('pk' ,)

    def __str__(self):
        return f'{self.pk} - {self.estoque.pk} - {self.produto}'
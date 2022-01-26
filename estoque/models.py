from tabnanny import verbose
from weakref import proxy
from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from django.urls import reverse_lazy
from estoque.managers import EstoqueEntradaManager, EstoqueSaidaManager
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
        return f'{self.pk} - {self.nf} - {self.created.strftime("%d- %m - %Y")}'

    def get_url(self):
        return reverse_lazy('estoque:estoque_entrada_detail' ,  kwargs= {'pk': self.pk})

    def nf_formated(self):
        return str(self.nf).zfill(10)


class EstoqueEntrada(Estoque):
    object = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque_entrada'
        verbose_name_plural = 'estoque_entrada'


    

class EstoqueSaida(Estoque):
    object = EstoqueSaidaManager()
    class Meta:
        proxy = True
        verbose_name = 'estoque_saida'
        verbose_name_plural = 'estoque'

class EstoqueItens(models.Model):
    estoque =models.ForeignKey( Estoque , on_delete= models.CASCADE , related_name= 'estoques')
    produto = models.ForeignKey(Product ,  on_delete=models.CASCADE)
    quantidade= models.PositiveBigIntegerField()
    saldo= models.PositiveSmallIntegerField()
    

    class Meta:
        ordering = ('pk' ,)

    def __str__(self):
        return f'{self.pk} - {self.estoque.pk} - {self.produto}'


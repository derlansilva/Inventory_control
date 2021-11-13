from django.db import models

# Create your models here.


class Product(models.Model):
    imported = models.BooleanField(default= True)
    ncm = models.CharField('NCM', max_length= 8)
    product = models.CharField(max_length=100 , unique=True)
    price = models.DecimalField('price' , max_digits=7 , decimal_places=2)
    inventory = models.IntegerField('current_inventory')
    minimum_inventory = models.IntegerField('minimum_inventory' ,default= 0)


    class Meta:
        ordering = ('product' , )


    def __str__(self) :
        return self.product

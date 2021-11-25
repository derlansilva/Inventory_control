import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE" ,   "inventory.settings")
django.setup()

import string
import timeit
from random import randint , random , choice
from product.models import Product


class Utils :
    '''METODOS GENERICOS'''
    ''' FUNÇÃO STATIC PARA GERAR NUMEROS ALEATORIOS'''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProductsClass:
    @staticmethod
    def create_products(produtos):
        Product.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                product = produto,
                imported = choice((True , False)),
                ncm= Utils.gen_digits(8),
                price = random()* randint(10 , 50),
                inventory = randint(10 , 200),
            )
            #os dois ** vai desempacotar o data dentro de Product
            obj = Product(**data)
            aux.append(obj)
        Product.objects.bulk_create(aux)

produtos = (
    'Apontador',
    'Caderno 100 folhas',
    'Caderno capa dura 200 folhas',
    'Caneta esferografica azul',
    'Caneta esferografica vermelha',
    'Caneta esferografica preta',
    'Regua',
    'Caderno de desenho',
    'Cartolina',
    'Mochila homem aranha',
    'Tesoura',
)

tic = timeit.default_timer()
ProductsClass.create_products(produtos)

toc = timeit.default_timer()

print('tempo', toc - tic)
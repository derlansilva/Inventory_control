from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    #aqui voce define as colunas que irão aparecer na tela admin
    list_display = (
        '__str__',
        'imported',
        'ncm',
        'price',
        'inventory',
        'minimum_inventory',
    )

    search_fields = ('product',)
    list_filter = ('imported',)
from re import search
from django.contrib import admin
from .models import Estoque, EstoqueEntrada , EstoqueItens, EstoqueSaida
 
# Register your models here.
class EstoqueItensAdmin(admin.TabularInline):
    model =  EstoqueItens
    estra = 0

@admin.register(EstoqueEntrada)

class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensAdmin , )
    list_display = ('__str__','nf','funcionario')
    search_fields =('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensAdmin)
    list_display = ('__str__' 'nf' , 'funcionario')
    search_filds = ('nf' ,)
    list_fielter = ('funcionario' , )
    date_hierarchy = 'created'

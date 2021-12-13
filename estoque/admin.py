from django.contrib import admin
from .models import Estoque , EstoqueItens
 
# Register your models here.
class EstoqueItensAdmin(admin.TabularInline):
    model =  EstoqueItens
    estra = 0

@admin.register(Estoque)

class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensAdmin , )
    list_display = (
        '__str__',
        'nf',
        'funcionario'
    )

    search_fields =('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


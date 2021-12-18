from django.shortcuts import render
from .models import Estoque

# Create your views here.
def entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento = 'e')
    context = {'object_list' : objects}
    return render(request  , template_name , context)
    
def entrada_detail(request , pk):
    template_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk = pk)
    context = {'object' : obj}
    return render(request , template_name , context )


def saida_list(request):
    template_name = 'estoque_saida_list.html'
    objects = Estoque.objects.filter(movimento = 's')
    context = {'object_list' : objects}
    return render(request  , template_name , context)


def saida_datail(request , pk):
    template_name = 'estoque_saida_detail.html'
    obj = Estoque.objects.get(pk = pk)
    context = {'object' : obj}
    return render(request , template_name  , context)
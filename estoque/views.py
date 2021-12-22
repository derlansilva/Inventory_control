from django.forms.models import inlineformset_factory
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render, resolve_url

from estoque.forms import EstoqueForm, EstoqueItensForm
from product.models import Product
from .models import Estoque, EstoqueItens

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

def entrada_form(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min = True,
    )

    if request.method =='POST':
        form = EstoqueForm(request.POST , instance= estoque_form , prefix='main')
        formset = item_estoque_formset(request.POST , instance= estoque_form , prefix= 'estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset = formset.save()
            dar_baixa_estoque(form)
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url , form.pk))
    else: 
        form = EstoqueForm(instance= estoque_form , prefix='main')
        formset = item_estoque_formset(instance= estoque_form , prefix='estoque')

    context = {'form' :form , 'formset': formset}
    return render(request , template_name , context)


def dar_baixa_estoque(form):
    produtos = form.estoques.all()
    print('form = ' ,form.estoques.all())
    for item in produtos:
        produto = Product.objects.get(pk = item.produto.pk)
        print('produto e igual' , produto.inventory) 
        produto.inventory = item.saldo
        produto.save()
    print("estoque atualizado com sucesso")

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
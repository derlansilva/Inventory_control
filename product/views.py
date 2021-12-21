from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView , UpdateView
from product.form import ProductForm
from .models import Product

# Create your views here.

def produto_list(request):
    template_name = 'produto_list.html'
    objects= Product.objects.all()
    context = {'object_list': objects}
    return render(request  , template_name , context)


def product_detail(request , pk):
    template_name = 'product_detail.html'
    obj = Product.objects.get(pk = pk)
    context = {'object_list' : obj}
    return render(request , template_name  , context )

def product_add(request):
    template_name = 'product_form.html'
    return render(request  , template_name)

def product_json(request , pk):
    '''Retorna o produto id e estoque'''
    produto = Product.objects.filter(pk= pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data' : data})

class ProductCreate(CreateView):
    model = Product
    template_name =   'product_form.html'
    form_class = ProductForm



class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm



from django.shortcuts import render
from .models import Product

# Create your views here.


def produto_list(request):
    template_name = 'produto_list.html'
    objects= Product.objects.all()
    context = {'object_list': objects}

    return render(request  , template_name , context)
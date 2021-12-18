from os import name
from django.urls import path
from django.utils.regex_helper import normalize

from estoque import views as v 


app_name = 'estoque'

urlpatterns =[
    path('' , v.entrada_list , name='entrada_list'),
    path('<int:pk>/' ,v.entrada_detail , name= 'estoque_entrada_detail'),
    path('add' , v.entrada_form , name='entrada_form'),

    path('exit/' , v.saida_list , name= 'saida_list'),
    path('exit/<int:pk>/' , v.saida_datail , name='estoque_saida_detail'),
]
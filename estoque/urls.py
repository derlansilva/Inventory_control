from os import name
from django.urls import path

from estoque import views as v 


app_name = 'estoque'

urlpatterns =[
    path('' , v.entrada_list , name='entrada_list'),
    path('exit/' , v.saida_list , name= 'saida_list'),
    path('<int:pk>/' ,v.entrada_detail , name= 'estoque_entrada_detail'),
    path('exit/<int:pk>/' , v.saida_datail , name='estoque_saida_detail'),
]
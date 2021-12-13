from django.urls import path

from estoque import views as v 


app_name = 'estoque'

urlpatterns =[
    path('' , v.entrada_list , name='entrada_list')
]
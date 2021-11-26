from django.urls import path
from product import views as v


app_name = 'produto'

urlpatterns = [
    path('' , v.produto_list)
]
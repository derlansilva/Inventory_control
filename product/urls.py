from django.urls import path
from product import views as v


app_name = 'produto'

urlpatterns = [
    path('' , v.produto_list , name='product_list'),
    path('<int:pk>/' , v.product_detail , name='product_detail'),
    path('add/' , v.product_add , name= 'product_add' ),
]
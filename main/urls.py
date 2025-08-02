from django.urls import path
from main.views import index, products, register, user_login, products_index, products_index_2

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:id>/', products, name='products'),

    path('products_index/<int:id>/', products_index, name='products_index'),
    path('products_index_2/<int:id>/', products_index_2, name='products_index_2'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]

from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<str:username>/', views.products_list, name='products_list'),
    path('<str:username>/<int:page>', views.products_list, name='products_list'),
    path('<str:username>/search/', views.products_list, name='products_list_search'),
    path('<str:username>/search/<int:page>', views.products_list, name='products_list_search'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
]

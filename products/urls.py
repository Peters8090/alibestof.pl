from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('p/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    
    path('user/<str:username>/', views.products_list, name='products_list'),
    path('user/<str:username>/page/<int:page>/', views.products_list, name='products_list'),

    path('user/<str:username>/search/', views.products_list, name='products_list_search'),
    path('user/<str:username>/search/page/<int:page>/', views.products_list, name='products_list_search'),

    path('user/<str:username>/custom_page/', views.products_list_pagination_custom_page_redirect,
         name='products_list_pagination_custom_page_redirect'),
]

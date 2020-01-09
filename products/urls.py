from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<str:username>/', views.user_profile_view, name='user_profile'),
    path('<str:username>/search/', views.user_profile_search_view, name='user_profile_search'),
]

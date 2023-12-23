from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('product_update/<int:product_id>/', views.upd_prod_form, name='product_update'),
    path('product_update_id/', views.upd_prod_id_form, name='product_update_id'),
]

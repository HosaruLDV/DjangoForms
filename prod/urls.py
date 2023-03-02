from django.urls import path
from django.views.decorators.cache import cache_page

from prod.apps import ProdConfig
from prod.views import *

app_name = ProdConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list')
]

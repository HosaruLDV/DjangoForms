from django.urls import path
from prod.apps import ProdConfig
from prod.views import *

app_name = ProdConfig.name

urlpatterns =[
    path('', ProductListView.as_view(), name = 'product'),
    path('product_create/', ProductCreateView.as_view(), name = 'product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name = 'product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name = 'product_delete')
]
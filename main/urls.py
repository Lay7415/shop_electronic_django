from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.main, name='main'),
    path('products/<int:id>/', views.product_detail_view, name='product_detail'),
]

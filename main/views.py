from django.shortcuts import render, get_object_or_404
from .models import ProductModel


def main(request):
    products_list = ProductModel.objects.all()
    print(products_list)

    return render(request, 'products/main.html', context={"products_list": products_list})


def product_detail_view(request, id):
    if request.method == 'GET':
        product = get_object_or_404(ProductModel, pk=id)
        return render(request, 'products/product_detail.html', {'product': product})

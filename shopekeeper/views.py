import csv
from collections import OrderedDict
from django.shortcuts import render, reverse, HttpResponse, redirect
from django.contrib import messages
from rest_framework import  generics
from .serializres import ProductSerializer
from .models import Products
from .forms import AddProductForm


def add_products(request):
    product_form = AddProductForm(request.POST, request.FILES)
    if request.method == 'POST':
        product_form = AddProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            products_file = request.FILES['products_file']
            decoded_file = products_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for product in reader:
                print(product['shopekeeper_id'])
                products_instance = Products()
                products_instance.name = product['name']
                products_instance.product = product['product']
                products_instance.description = product['description']
                products_instance.price = product['price']
                products_instance.shopekeeper_id = product['shopekeeper_id']
                products_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added the product details')
            return redirect(reverse('add-products'))
        else:
            messages.add_message(request, messages.DANGER, 'Error try agin')
            return redirect(reverse('add-products'))
    return render(request, 'shopekeeper/add-product.html', {'form': product_form})

class ListProductsAPI(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, **kwargs):
        shopekeeper_id = self.kwargs['shopekeeper_id']
        products = Products.objects.filter(shopekeeper_id=shopekeeper_id)
        return products





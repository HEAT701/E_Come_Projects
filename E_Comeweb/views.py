from Ecome.models import Product
from Ecome.forms import ProductForm
from django.shortcuts import render

def vews_product(request):
    products = Product.objects.all()
    print(products)
    return render(request,'Home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
     form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
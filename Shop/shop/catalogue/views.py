from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required 


def list_products(request):
    products = Product.objects.all()
    return render(request, 'catalogue/product.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "catalogue/product_details.html", {"product": product})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        cart[str(product.id)] = cart.get(str(product.id), 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
        return redirect('cart_detail')
    else:
        return redirect('product_detail', id=product_id)


def cart_detail(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total = 0
    for product_id_str, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id_str))
        except Product.DoesNotExist:
            continue
        subtotal = product.price * quantity
        total += subtotal
        products_in_cart.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'catalogue/cart_detail.html', {'products': products_in_cart, 'total': total})


def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)
        if product_id_str in cart:
            del cart[product_id_str]
            request.session['cart'] = cart
            request.session.modified = True
        return redirect('cart_detail')
    else:
        return redirect('cart_detail')


@login_required 
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect("catalogue:list_products")
    else:
        form = ProductForm()

    return render(request, "catalogue/create_product.html", {"form": form})

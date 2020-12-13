from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from parksystemapp.models import Reservation
from .cart import Cart
# from .forms import CartAddProductForm <-- don't think I need it

# Create your views here.
@require_POST
def cart_add(request, reservation_id):
    cart = Cart(request)
    product = get_object_or_404(Reservation, id=reservation_id)
    # form = CartAddProductForm(request.POST) <-- don't need?
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, reservation_id):
    cart = Cart(request)
    product = get_object_or_404(Reservation, id=reservation_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})
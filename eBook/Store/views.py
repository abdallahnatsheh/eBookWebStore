from django.shortcuts import render, HttpResponseRedirect
from .models import Ebook, CartItems
from django.views.decorators.csrf import csrf_exempt


def store_view(request):
    ebooks = {'eBooks' : Ebook.objects.all()}
    return render(request, 'Store\index.html', ebooks)


def cart_view(request):
    CART_ITEMS = CartItems.objects.all()
    cart_total = 0
    for item in CART_ITEMS:
        cart_total += item.price
    return render(request, 'Store\cart.html', {
        'cart_items' : CART_ITEMS,
        'cart_total' : cart_total
    })


@ csrf_exempt
def add_cart_item(request):
    book_id = request.POST['book_id']
    title = Ebook.objects.get(pk=book_id).title
    price = Ebook.objects.get(pk=book_id).price
    item = CartItems.objects.create(title=title, price=price)
    return HttpResponseRedirect('/store')


@ csrf_exempt
def del_cart_item(request):
    item_id = request.POST['item_id']
    CartItems.objects.get(pk=item_id).delete()
    return HttpResponseRedirect('/store/cart')
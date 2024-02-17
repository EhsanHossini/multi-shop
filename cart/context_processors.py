from .cart_module import Cart


def cart(request):
    return {'cart': Cart(request)}

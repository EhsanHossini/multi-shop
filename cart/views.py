from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from accounts.models import Address
from products.models import Product
from .cart_module import Cart
from .models import Order, OrderItem, DiscountCode
from .mixin import UserLoginDetail
from django.http import HttpResponse
import requests
import json
from .forms import AddToCartProductForm


class CartDetailView(UserLoginDetail, View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['product_update_quantity_form'] = AddToCartProductForm(initial={
                'quantity': item['quantity'],
                'inplace': True,
            })
        return render(request, "cart/cart_detail.html", {'Cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            size, color, quantity = request.POST.get("size", 'size'), request.POST.get("color", 'color'), request.POST.get("quantity")
            cart.add(product, quantity, color, size, replace_current_quantity=cleaned_data['inplace'])
        return redirect("cart:cart_detail")


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=id)
        cart.remove(id)
        return redirect("cart:cart_detail")


class OrderDetailView(UserLoginDetail, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'cart/order_detail.html', {'order': order})


class OrderCreationView(UserLoginDetail, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     quantity=item['quantity'], price=item['price'])
        cart.remove_cart()
        return redirect('cart:order_detail', order.id)


class ApplyDiscountView(UserLoginDetail, View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect("cart:order_detail", order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity = 1
        discount_code.save()
        return redirect("cart:order_detail", order.id)


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


class SendRequestView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk, user=request.user)
        address = get_object_or_404(Address, id=request.POST.get("address"))
        order.address = f"{address.address} - {address.phone} - {address.email}"
        order.save()
        request.session["order_id"] = str(order.id)
        req_data = {
            "merchant_id": MERCHANT,
            "amount": order.total_price,
            "callback_url": CallbackURL,
            "description": description,
            "metadata": {"mobile": request.user.number}
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


class VreIfyView(View):
    def get(self, request):
        t_status = request.GET.get('Status')
        t_authority = request.GET['Authority']
        order_id = request.session['order_id']
        order = Order.objects.get(id=int(order_id))
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.total_price,
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    order.is_paid = True
                    order.save()
                    return HttpResponse('Transaction success.\nRefID: ' + str(
                        req.json()['data']['ref_id']
                    ))
                elif t_status == 101:
                    return HttpResponse('Transaction submitted : ' + str(
                        req.json()['data']['message']
                    ))
                else:
                    return HttpResponse('Transaction failed.\nStatus: ' + str(
                        req.json()['data']['message']
                    ))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return HttpResponse('Transaction failed or canceled by user')
# 


from django.views.generic import TemplateView

from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .models import Medcart, Medicine_inventory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from django.http import HttpResponseBadRequest








from .models import DeviceInformation, Divicecart




from django.utils.functional import SimpleLazyObject



@login_required(login_url='/login/')
def add_to_cart(request, id):

    if request.user.is_authenticated:
   
        try:
            device = DeviceInformation.objects.get(id=id)
            print(device)
        except DeviceInformation.DoesNotExist:
            return HttpResponseNotFound("Device does not exist")

        user = request.user

        existing_cart_item = Divicecart.objects.filter(user=user, device=device).first()
        if existing_cart_item:
            existing_cart_item.quantity = 1
            existing_cart_item.save()
        else:
            Divicecart.objects.create(user=user, device=device, quantity=1)

        return redirect("cart_view")
    else:

        return HttpResponse("Hello, please log in.")


def cart_view(request):
    user = request.user
    cart = Divicecart.objects.filter(user=user)
    total = 0
    for item in cart:
        total += item.quantity * item.device.price

    return render(request, "cart/add_to_cart.html", {'cart': cart, 'total': total})


# from django.shortcuts import get_object_or_404


def devremove_cart_item(request, id):
    cart_item = get_object_or_404(Divicecart, id=id)

    cart_item.delete()
   

    return redirect('cart_view')

from django.shortcuts import render, redirect
from .models import Divicecart, Order

# def OrderForm(request):
#     if request.method == "POST":
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         user_details = Address.objects.create(address=address, phone=phone)
#         user_details.save()

#         user = request.user
#         cart_items = Divicecart.objects.filter(user=user)
#         total = 0

#         for cart_item in cart_items:
#             total += cart_item.quantity * cart_item.device.price
#             Order.objects.create(
#                 user=user,
#                 address=address,
#                 phone=phone,
#                 device=cart_item.device,
#                 no_of_items=cart_item.quantity,
#                 order_status="paid",
#                 total_price=total
#             )

#         cart_items.delete()    
#         return redirect("order_confirm_view")

#     return render(request, "cart/order.html")

from django.shortcuts import render, redirect
from .models import Address, Divicecart, Order

def OrderForm(request):
    if request.method == "POST":
        # Get form data
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Create user details
        user_details = Address.objects.create(address=address, phone=phone)

        # Get user and cart items
        user = request.user
        cart_items = Divicecart.objects.filter(user=user)
        total = 0

        # Create orders for each cart item
        for cart_item in cart_items:
            total += cart_item.quantity * cart_item.device.price
            Order.objects.create(
                user=user,
                address=address,
                phone=phone,
                device=cart_item.device,
                no_of_items=cart_item.quantity,
                order_status="paid",
                total_price=total
            )

            # Delete the corresponding device from DeviceInformation
            cart_item.device.delete()

        # Delete cart items after creating orders
        cart_items.delete()    
        return redirect("order_confirm_view")

    return render(request, "cart/order.html")




def order_confirm_view(request):
    return render(request, "cart/order_confirm.html")







@login_required(login_url='/login/')
def medadd_to_cart(request, id):
    user = request.user

    medicine = get_object_or_404(Medicine_inventory, id=id)
    try:
        cart_item = Medcart.objects.get(user=user, medicine=medicine)
        if cart_item.quantity < medicine.quanity_availble:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(request, "Sorry, this product is out of stock.")
    except Medcart.DoesNotExist:
        if medicine.quanity_availble > 0:
            cart_item = Medcart.objects.create(user=user, medicine=medicine, quantity=1)
            cart_item.save()
        else:
            messages.error(request, "Sorry, this product is out of stock.")
    return redirect('med_cart_view')


def med_cart_view(request):
    total = 0
    user = request.user
    cart = Medcart.objects.filter(user=user)
    for item in cart:
        total += item.quantity * item.medicine.price
    return render(request, 'cart/medicine_cart_view.html', {'cart': cart, 'total': total})



from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse

def itemcart_remove(request,id):
    try:
        med = Medicine_inventory.objects.get(id=id)
        print(med)
    except Medicine_inventory.DoesNotExist:
        raise Http404("Medicine inventory with id {} does not exist".format(id))
    # product=Medicine_inventory.objects.get(id=id)
    user=request.user
    try:
        cart=Medcart.objects.get(user=user,medicine=med)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()

        else:
            cart.delete()

    except:
        pass
    return redirect('med_cart_view')

from cart.form import PaymentForm

from django.shortcuts import render, redirect
from .models import Account, Medcart, MedicineOrder

from django.shortcuts import render, redirect
from .models import Account, Medcart, MedicineOrder

from django.http import Http404

@login_required(login_url='/login/')
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            accnumber = form.cleaned_data['accnumber']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']

            user = request.user
            cart = Medcart.objects.filter(user=user)
            total = sum(item.quantity * item.medicine.price for item in cart)

            try:
                acct = Account.objects.get(accnumber=accnumber)
            except Account.DoesNotExist:
                msg = "Account doesn't exist. Please enter a valid account number."
                return render(request, 'cart/successmed.html', {'msg': msg})

            if acct.balance >= total:
                for item in cart:
                    order = MedicineOrder.objects.create(
                        user=user,
                        address=address,
                        phone=phone,
                        medicine=item.medicine,
                        no_of_items=item.quantity,
                        order_status="paid",
                        total_price=item.quantity * item.medicine.price
                    )
                    order.save()
                    item.medicine.quanity_availble -= item.quantity
                    item.medicine.save()

                # Deduct total from account balance
                acct.balance -= total
                acct.save()

                # Clear the cart
                cart.delete()

                msg = 'Order placed successfully'
                return render(request, 'cart/successmed.html', {'msg': msg, 'total': total})
            else:
                msg = "Insufficient balance. You can't place the order."
                return render(request, 'cart/successmed.html', {'msg': msg, 'total': total})
        
            
        

    else:
        form = PaymentForm()
        user = request.user
        cart = Medcart.objects.filter(user=user)
        total = sum(item.quantity * item.medicine.price for item in cart)

    return render(request, 'cart/orderform.html', {'form': form})

@login_required(login_url='/login/')
def order_view(request):
    user = request.user
    orders = MedicineOrder.objects.filter(user=user)
    return render(request,'cart/order_view.html', {'orders': orders})





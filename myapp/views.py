from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import Product
from .models import Pickle
from .models import powder
from .models import PreMix
from .models import Papad
from .models import Snacks
from django.contrib import messages
from django.contrib.sessions.models import Session

def home(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})  
    return render(request, 'home.html', {'products': products, 'cart': cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {'name': product.name, 'price': float(product.price_1kg), 'quantity': 1}

    request.session['cart'] = cart 
    return redirect('home')  



def pickle_list(request):
    pickles = Pickle.objects.all()
    return render(request, 'pickle.html', {'pickles': pickles})

def add_to_cart(request, product_id):
    pickle = get_object_or_404(Pickle, id=product_id)
    return redirect('myapp:pickles')



def powder_list(request):
    powders = powder.objects.all() 
    return render(request, 'powders.html', {'powders': powders})  

def add_to_cart(request, product_id):
    product = get_object_or_404(powder, id=product_id)  
    return redirect('myapp:powders')  


def papads_list(request):
    papadss = Papad.objects.all()
    return render(request, 'papads.html', {'papadss': papadss})

def add_to_cart(request, papad_id):
    papad = get_object_or_404(Papad, id=papad_id)
    cart = request.session.get('cart', {})

    if papad_id in cart:
        cart[papad_id] += 1
    else:
        cart[papad_id] = 1

    request.session['cart'] = cart
    messages.success(request, f"{papad.name} added to cart!")
    return redirect('myapp:papads_list')


def pre_mixes_list(request):
    pre_mixess = PreMix.objects.all()
    return render(request, 'pre_mixes.html', {'pre_mixess': pre_mixess})

def add_to_cart(request, premix_id):
    premix = get_object_or_404(PreMix, id=premix_id)
    cart = request.session.get('cart', {})
    
    if premix_id in cart:
        cart[premix_id] += 1
    else:
        cart[premix_id] = 1
    
    request.session['cart'] = cart
    messages.success(request, f"{premix.name} added to cart!")
    return redirect('myapp:pre_mixes_list')

def snacks_list(request):
    snackss = Snacks.objects.all()  
    return render(request, 'snacks.html', {'snackss': snackss})

def search(request):
    form = SearchForm(request.GET or None)  

    if form.is_valid():
        query = form.cleaned_data['query'].strip().lower()

        search_mapping = {
            "pickels": "myapp:pickels",
            "powders": "myapp:powders",
            "papads": "myapp:papads",
            "pre_mixes": "myapp:pre_mixes",
            "snacks": "myapp:snacks",
            
        }

        if query in search_mapping:
            return redirect(search_mapping[query])

    return render(request, 'search.html', {'form': form, 'error': 'No matching product found. Please try again.'})


def cart(request):
    return render(request,'cart.html')

def join(request):
    return render(request, 'join.html')

def Avakaya(request):
    return render(request,'Avakaya.html')

def Tomato(request):
    return render(request,'Tomato.html')

def Magaya(request):
    return render(request,'Magaya.html')


def Gongura(request):
    return render(request,'Gongura.html')

def Nimmakaya(request):
    return render(request,'Nimmakaya.html')

def Allam(request):
    return render(request,'Allam.html')


def Karivepaku(request):
    return render(request,'Karivepaku.html')

def Kandi(request):
    return render(request,'Kandi.html')

def Nuvvula(request):
    return render(request,'Nuvvula.html')

def PalliPodi(request):
    return render(request,'PalliPodi.html')

def Nallakaram(request):
    return render(request,'Nallakaram.html')

def Appadalu(request):
    return render(request,'Appadalu.html')

def Saggu(request):
    return render(request,'Saggu.html')

def Biyyam(request):
    return render(request,'Biyyam.html')

def Gummadi(request):
    return render(request,'Gummadi.html')

def Challa(request):
    return render(request,'Challa.html')

def Pulihora(request):
    return render(request,'Pulihora.html')

def Palli(request):
    return render(request,'Palli.html')

def Putnala(request):
    return render(request,'Putnala.html')

def Ragi(request):
    return render(request,'Ragi.html')

def Adai(request):
    return render(request,'Adai.html')

def Boondimixture(request):
    return render(request,'Boondimixture.html')

def Muruku(request):
    return render(request,'Muruku.html')

def Chegodi(request):
    return render(request,'Chegodi.html')

def Masala(request):
    return render(request,'Masala.html')

def Boondi(request):
    return render(request,'Boondi.html')


def our_pickel(request):
    return render(request, 'our_pickel.html')

def sustain_pack(request):
    return render(request,'sustain_pack.html')



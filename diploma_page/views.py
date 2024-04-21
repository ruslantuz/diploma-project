from django.http import HttpResponseRedirect
from django.shortcuts import render
from diploma_page.models import Destinations, Orders, Trips#Offers, Planners
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import AccountCreationForm, OrderForm
from diploma_page import forms

def index(request):
    data = Trips.objects.all()
    dest = Destinations.objects.all()
    form = registerForm(request)
    order_form = createOrderForm(request, data)

    return render(request, 'index.html', {'data': data, 'dest':dest,'form': form, 'order_form':order_form })

def registerForm(request):
    if request.method == "POST" and 'login' in request.POST:
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            messages.error(request, form.errors, extra_tags="register")
    else:
        form = AccountCreationForm()
    return form

@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate = True, no_store = True)

def Login(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Orders.objects.filter(status = "pending" or "confirmed").filter(user = user.id)
        orders = orders.order_by('-status')
        
        admin_orders = Orders.objects.filter(status = "pending")
        return render(request, 'user_page/index.html', {'user':user, 'orders':orders, 'admin_orders':admin_orders})

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect("login/")
        else:
            messages.error(request, "Enter your data correctly.", extra_tags="login")
            return HttpResponseRedirect("/")

def LogOut(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect("/")

def blogs(request):
    form = registerForm(request)
    return render(request, 'blog_page/index.html', {'form': form})

def offer_item(request, id):
    data = Trips.objects.get(id = id)
    order_form = createOrderForm(request, data)
    form = registerForm(request)    
    return render(request, 'offer-page/index.html', {'data': data, 'form': form, 'order_form': order_form})

def offers(request):
    data = Trips.objects.all()
    form = registerForm(request)
    return render(request, 'offers/index.html', {'data': data,'form': form})
    
def createOrderForm(request, data):
    if request.method == 'POST':
        if 'order' in request.POST:
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                print("if order_form.is_valid():")
                # Save the order
                order = order_form.save(commit=False)
                order.user = request.user
                try:
                    order.trip                        
                except:
                    order.trip = data
                # ?????????????????????'
                    
                order.save()
                # Optionally, add a success message
                messages.success(request, "Order placed successfully!")
                return HttpResponseRedirect('/')  # Redirect after successful order placement
    else:
        order_form = OrderForm()
    return order_form


def CancelOrder(request):
    if request.method == "POST":
        id = request.POST.get('id') 
        order = Orders.objects.filter(id=id).update(status = "cancelled")
        return HttpResponseRedirect("/login")

def ConfirmOrder(request):
    if request.method == "POST":
        id = request.POST.get('id') 
        order = Orders.objects.filter(id=id).update(status = "confirmed")
        return HttpResponseRedirect("/login")

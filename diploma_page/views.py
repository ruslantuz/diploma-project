from django.http import HttpResponseRedirect
from django.shortcuts import render
from diploma_page.models import Blog, Destinations, Orders, Reviews, Trips
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import AccountCreationForm, OrderForm, ReviewForm
from diploma_page import forms
from django.db.models import Q

def index(request):
    data = Trips.objects.all()
    dest = Destinations.objects.all()
    blog = Blog.objects.order_by('?')[0]
    reviews = Reviews.objects.all()
    if request.user.is_anonymous:
        order_form = OrderForm()
        if request.method == 'POST' and 'login' not in request.POST:
            messages.error(request, "You are not logged in!", extra_tags="not_logged")
    else:
        order_form = createOrderForm(request, data)

    form = registerForm(request)
    return render(request, 'index.html', {'data': data, 'dest':dest, 'reviews' : reviews,'form': form, 'order_form':order_form,'blog':blog})

def registerForm(request):
    if request.method == "POST" and 'login' in request.POST:
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!", extra_tags="register_success")
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
        orders = Orders.objects.filter(Q(status = "pending") | Q(status = "confirmed")).filter(user = user.id)
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
            messages.success(request, "Login successfully!", extra_tags="login_success")
            return HttpResponseRedirect("login/")
        else:
            messages.error(request, "Enter your data correctly.", extra_tags="login")
            return HttpResponseRedirect("/")

def LogOut(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect("/")

def blogs(request, id):
    form = registerForm(request)
    blog = Blog.objects.get(id = id)
    return render(request, 'blog_page/index.html', {'form': form, 'blog':blog})

def offer_item(request, id):
    data = Trips.objects.get(id = id)
    reviews = Reviews.objects.filter(trip = id)
    
    if request.user.is_anonymous:
        order_form = OrderForm()
        review_form = ReviewForm()
        if request.method == 'POST' and 'login' not in request.POST:
            messages.error(request, "You are not logged in!", extra_tags="not_logged")
    else:
        order_form = createOrderForm(request, data)
        if request.method == 'POST' and request.user.is_anonymous != True:
            if 'review' in request.POST:
                review_form = ReviewForm(request.POST)
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.user = request.user
                    try:
                        review.trip                        
                    except:
                        review.trip = data
                    review.save()
                    messages.success(request, "Review posted successfully!", extra_tags="review_success")
                    return HttpResponseRedirect('/')  # Redirect after successful order placement
        else:
            review_form = ReviewForm()


    form = registerForm(request)    
    return render(request, 'offer-page/index.html', {'data': data, 'reviews':reviews, 'form': form, 'order_form': order_form, 'review_form':review_form})

def offers(request):
    data = Trips.objects.all()
    form = registerForm(request)
    return render(request, 'offers/index.html', {'data': data,'form': form})
    
def createOrderForm(request, data):
    if request.method == 'POST' and 'order' in request.POST:
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            try:
                order.trip                        
            except:
                order.trip = data
                
            order.save()
            messages.success(request, "Order placed successfully!", extra_tags="order_success")
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

from django.http import HttpResponseRedirect
from django.shortcuts import render
from diploma_page.models import Destinations, Offers, Planners
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import AccountCreationForm

def index(request):
    data = Offers.objects.all()
    dest = Destinations.objects.all()
    planners = Planners.objects.all()
    form = registerForm(request)
    return render(request, 'index.html', {'data': data, 'dest':dest , 'planners' : planners ,'form': form})

def registerForm(request):
    if request.method == "POST":
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
        return render(request, 'user_page/index.html', {'user':user})

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
    data = Offers.objects.get(id = id)
    form = registerForm(request)
    return render(request, 'offer-page/index.html', {'data': data, 'form': form})
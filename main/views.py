from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from cart.forms import AddProductForm
from main.forms import AddCar, RegistrationForm, LoginForm, NewloginForm, NewPasswordForm
from main.models import Car, Brand, Manufacturer
from orders.models import Order


# Create your views here.
def get_page(request):
    cars = Car.objects.select_related('brand').all()
    brand = Brand.objects.all()
    manufacturer = Manufacturer.objects.all()
    context = {
        'cars': cars,
        # 'brand': brand,
        # 'manufacturer': manufacturer,
    }
    return render(request, 'main.html', context)

def get_brand(request):
    brand_car = Car.objects.filter(brand=request.GET.get('brand'))
    brand = Brand.objects.select_related('car').all()
    manufacturer = Manufacturer.objects.all()
    manuf_car = Car.objects.filter(manufacturer=request.GET.getlist('manufacturer'))
    context = {
        'cars': brand_car if brand_car else manuf_car,
        # 'brand': brand,
        # 'manufacturer': manufacturer,
    }
    # if request.GET.get('brand'):
    #     context = {
    #         'cars': brand_car,
    #         'brand': brand,
    #         'manufacturer': manufacturer,
    #     }
    # if request.GET.get('manufacturer'):
    #     context = {
    #         'cars': manuf_car,
    #         'brand': brand,
    #         'manufacturer': manufacturer,
    #     }

    return render(request, 'brand.html', context)

def get_add_car(request):
    forms = AddCar()
    car_all = Car.objects.all()

    if request.method =='POST':
        forms = AddCar(request.POST,request.FILES)
        if forms.is_valid():
            print(forms.cleaned_data)
            forms.save()
            return redirect('Home')
    context = {
        'forms': forms,
        'car_all': car_all,
    }
    return render(request, 'add_car.html', context)





def detail_info(request, id):
    car = Car.objects.get(id=id)
    cars = Car.objects.all()
    form = AddProductForm()
    context = {
        'car': car,
        'cars': cars,
        'form': form,
    }
    return render(request, 'detail.html', context)

def search(request):
    results = Car.objects.filter(brand__title__icontains=request.GET.get('search')) | Car.objects.filter(description__icontains=request.GET.get('search'))
    context = {
       'cars': results,
    }
    return render(request, 'search_result.html', context)



def registration(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            # User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            user.save()
            return redirect('Home')
    context = {
        'form': form,
    }
    return render(request, 'registration.html', context)

def login_user(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('Home')
            else:
                error_message = 'Не правильные данные'
                context = {
                    'form': form,
                    'error_message': error_message
                }
    return render(request, 'login.html', context)

def logaut_user(request):
    logout(request)
    return redirect('Home')
@login_required
def kabinet(request):
    new_log = NewloginForm(initial={'username': request.user.username})

    pass_form = NewPasswordForm()
    context = {
        'log_form': new_log,
        'pass_form': pass_form,

    }
    if request.method == 'POST':
        new_log = NewloginForm(request.POST)
        pass_form = NewPasswordForm(request.POST)
        if request.POST.get('username'):
            if new_log.is_valid():
                user = request.user
                user.username = new_log.cleaned_data.get('username')
                user.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'new_username': user
                }
        if request.POST.get('password'):
            if pass_form.is_valid():
                user_pass = request.user
                user_pass.set_password(pass_form.cleaned_data.get('password'))
                user_pass.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'user_pass': user_pass
                }
    return render(request, 'kabinet.html', context)

def my_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    print(orders)
    context={
        'orders': orders,

    }
    return render(request, 'kabinet.html', context)


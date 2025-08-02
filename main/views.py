from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from main.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



def index(request):
    ctx = {
        'categoriya': Categoriya.objects.all(),
        'product_2': Productos.objects.all(),
    }
    return render(request, 'main/index.html', ctx)


def products_index(request, id):
    ctx = {
        "product_2": Productos.objects.filter(category_id=id),
        'categoriya': Categoriya.objects.all(),

        'product': Productos.objects.filter(category_id=id),
    }
    return render(request, 'main/index.html', ctx)


def products_index_2(request, id):
    ctx = {
        "product_2": Productos.objects.filter(category_id=id),
        'categoriya': Categoriya.objects.all(),

        'product': Productos.objects.filter(category_id=id),
    }
    return render(request, 'main/index.html', ctx)







def products(request, id):
    ctx = {
        'product':  Productos.objects.filter(category_id=id),
        'categoriya': Categoriya.objects.all(),
        'product_2': Productos.objects.all(),

    }
    b = []
    my_string = ""
    a = ctx['product']
    for i in a.filter(id=id):
        b.append(i.category.name)
    for item in b:
        my_string += item + ""
    my_string = my_string.strip()  # "Salom dunyo"
    ctx['b'] = my_string

    return render(request, 'main/store.html', ctx, )




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:

            form = AuthenticationForm()
            return render(request, 'main/login.html', {'form': form, 'error': 'Foydalanuvchi nomi yoki parol noto\'g\'ri.'})
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
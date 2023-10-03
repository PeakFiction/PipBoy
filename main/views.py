from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required(login_url='/login')
def show_main(request):  
    items = Product.objects.filter(user=request.user).order_by('-id')  # Newest item first

    # Mark the newest item as is_new=True and all others as is_new=False
    if items:
        newest_item = items[0]
        newest_item.is_new = True
        newest_item.save()
        for item in items[1:]:
            item.is_new = False
            item.save()

    context = {
        'AppName': 'Pip-Boy!',
        'name': request.user.username,
        'class': 'PBP KI',
        'description': "From the innovative minds at Vault-Tec, we proudly present the Pip-Boy Inventory Manager, a cutting-edge web-based solution designed to enhance your post-apocalyptic survival experience. Just like its wrist-mounted predecessor, the Pip-Boy Inventory Manager offers seamless access to your crucial inventory data. Seamlessly navigate your stash of equipment, manage your consumables, and keep tabs on your quest progress, all from the comfort of your preferred device's web browser. Vault-Tec's commitment to user-friendly design ensures that you can effortlessly organize your post-apocalyptic life, whether it's keeping track of your precious bottle caps or maintaining your arsenal of weaponry. Surviving the wasteland has never been this organized, thanks to the Pip-Boy Inventory Manager—a technological marvel for the modern survivor.",
        'version': "Pip-Boy 3000 Mark IV Web Version",
        'releasedate': "2287",
        'items': items,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.is_new = True  # Set the is_new attribute to True for newly added items
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product by ID
    product = Product.objects.get(pk = id)

    # Set product as instance of form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save the form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get data by ID
    product = Product.objects.get(pk=id)
    # Delete data
    product.delete()
    # Return to the main page
    return HttpResponseRedirect(reverse('main:show_main'))

def show_about(request):
    return render(request, 'about.html')

def increment_item(request, id):
    item = Product.objects.get(pk = id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_item(request, id):
    item = Product.objects.get(pk = id)
    item.amount -= 1
    if item.amount <= 0:
        item.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))




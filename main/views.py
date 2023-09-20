from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):  
    item = Product.objects.all()
    
    context = {
        'AppName': 'Pip-Boy!',
        'name': 'Muhammad Sakhran',
        'class': 'PBP KI',
        'description': "From the innovative minds at Vault-Tec, we proudly present the Pip-Boy Inventory Manager, a cutting-edge web-based solution designed to enhance your post-apocalyptic survival experience. Just like its wrist-mounted predecessor, the Pip-Boy Inventory Manager offers seamless access to your crucial inventory data. Seamlessly navigate your stash of equipment, manage your consumables, and keep tabs on your quest progress, all from the comfort of your preferred device's web browser. Vault-Tec's commitment to user-friendly design ensures that you can effortlessly organize your post-apocalyptic life, whether it's keeping track of your precious bottle caps or maintaining your arsenal of weaponry. Surviving the wasteland has never been this organized, thanks to the Pip-Boy Inventory Manager—a technological marvel for the modern survivor.",
        'version': "Pip-Boy 3000 Mark IV Web Version",
        'releasedate': "2287",
        'items': item
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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
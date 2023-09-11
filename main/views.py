from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'AppName': 'Pip-Boy!',
        'name': 'Muhammad Sakhran',
        'class': 'PBP KI',
        'description': "From the innovative minds at Vault-Tec, we proudly present the Pip-Boy Inventory Manager, a cutting-edge web-based solution designed to enhance your post-apocalyptic survival experience. Just like its wrist-mounted predecessor, the Pip-Boy Inventory Manager offers seamless access to your crucial inventory data. Seamlessly navigate your stash of equipment, manage your consumables, and keep tabs on your quest progress, all from the comfort of your preferred device's web browser. Vault-Tec's commitment to user-friendly design ensures that you can effortlessly organize your post-apocalyptic life, whether it's keeping track of your precious bottle caps or maintaining your arsenal of weaponry. Surviving the wasteland has never been this organized, thanks to the Pip-Boy Inventory Manager—a technological marvel for the modern survivor.",
        'version': "Pip-Boy 3000 Mark IV Web Version",
        'releasedate': "2287"
    }

    return render(request, 'main.html', context)
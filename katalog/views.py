from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_item_katalog,
        'nama': 'Rifqi Farel Muhammad',
        'id' : '2106650310'
    }
    return render(request, "katalog.html", context)
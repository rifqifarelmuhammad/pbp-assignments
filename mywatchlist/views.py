from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MywatchlistItem.objects.all()
    context = {
        'list_film': data_mywatchlist,
        'nama': 'Rifqi Farel Muhammad',
        'id' : '2106650310'
    }

    return render(request, "mywatchlist.html", context)

def show_mywatchlist_HTML(request):
    data_mywatchlist = MywatchlistItem.objects.all()
    context = {
        'list_film': data_mywatchlist
    }

    return render(request, "html_mywatchlist.html", context)

def show_mywatchlist_XML(request):
    data_mywatchlist = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_JSON(request):
    data_mywatchlist = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
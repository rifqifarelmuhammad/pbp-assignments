from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    length_watched = data_mywatchlist.filter(watched = True)
    length_not_watched = data_mywatchlist.filter(watched = False)

    if (len(length_watched) >= len(length_not_watched)):
        context = {
            'list_film': data_mywatchlist,
            'nama': 'Rifqi Farel Muhammad',
            'id' : '2106650310',
            'pesan': "Selamat, kamu sudah banyak menonton!"
        }
    else:
        context = {
            'list_film': data_mywatchlist,
            'nama': 'Rifqi Farel Muhammad',
            'id' : '2106650310',
            'pesan': "Wah, kamu masih sedikit menonton!"
        }

    return render(request, "mywatchlist.html", context)

def show_mywatchlist_HTML(request):
    data_mywatchlist = MyWatchList.objects.all()
    length_watched = data_mywatchlist.filter(watched = True)
    length_not_watched = data_mywatchlist.filter(watched = False)

    if (len(length_watched) >= len(length_not_watched)):
        context = {
            'list_film': data_mywatchlist,
            'pesan': "Selamat, kamu sudah banyak menonton!"
        }
    else:
        context = {
            'list_film': data_mywatchlist,
            'pesan': "Wah, kamu masih sedikit menonton!"
        }

    return render(request, "html_mywatchlist.html", context)

def show_mywatchlist_XML(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_JSON(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
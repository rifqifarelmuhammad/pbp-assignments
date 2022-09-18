from django.urls import path
from mywatchlist.views import show_mywatchlist_HTML
from mywatchlist.views import show_mywatchlist_XML
from mywatchlist.views import show_mywatchlist_JSON

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist_HTML, name='show_mywatchlist_HTML'),
    path('xml/', show_mywatchlist_XML, name='show_mywatchlist_XML'),
    path('json/', show_mywatchlist_JSON, name='show_mywatchlist_JSON'),
]
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):
    def test_show_mywatchlist_HTML(self):
        self.client = Client()
        self.mywatchlisthtml_url = reverse('mywatchlist:show_mywatchlist_HTML')

        response = self.client.get(self.mywatchlisthtml_url)
        self.assertEquals(response.status_code, 200)
    
    def test_show_mywatchlist_XML(self):
        self.client = Client()
        self.mywatchlistxml_url = reverse('mywatchlist:show_mywatchlist_XML')

        response = self.client.get(self.mywatchlistxml_url)
        self.assertEquals(response.status_code, 200)

    def test_showS_mywatchlist_JSON(self):
        self.client = Client()
        self.mywatchlistjson_url = reverse('mywatchlist:show_mywatchlist_JSON')

        response = self.client.get(self.mywatchlistjson_url)
        self.assertEquals(response.status_code, 200)
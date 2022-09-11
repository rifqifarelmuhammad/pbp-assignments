from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
    def test_should_create_catalog(self):
        self.project1 = CatalogItem.objects.create(
            item_name = "iPhone 12 Pro Max",
            item_price = 17999999,
            item_stock = 3,
            description = "Original from iBox",
            rating = 5,
            item_url = "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
        )

        testing = CatalogItem.objects.get(pk=1)

        self.assertEquals(self.project1, testing)
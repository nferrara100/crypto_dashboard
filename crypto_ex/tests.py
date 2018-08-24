from django.test import TestCase
from django.urls import reverse
from crypto_ex.views import get_coin_exchanges


class HomePageTest(TestCase):
    coin_exchanges = None
    test_coins = ["BTC", "SMART", "GBP"]

    def setUp(self):
        self.coin_exchanges = get_coin_exchanges()

    def test_index_load(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_data_exists(self):
        for coin in self.test_coins:
            self.assertIsNotNone(self.coin_exchanges[coin])

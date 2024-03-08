from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Popcorn", price=8.99, inventory=100)
        Menu.objects.create(title="Fish Stick", price=4.99, inventory=100)

    def test_getall(self):
        popcorn = Menu.objects.get(title="Popcorn")
        fish = Menu.objects.get(title="Fish Stick")
        popcorn_str = popcorn.__str__()
        self.assertEqual(popcorn_str, "Popcorn : 8.99")

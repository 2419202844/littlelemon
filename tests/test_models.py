from django.test import TestCase
from restaurant.models import Menu  # Imports your Menu model

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a temporary test instance of Menu
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        
        # Check if the string representation matches what we expect
        self.assertEqual(str(item), "IceCream : 80")
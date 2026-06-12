from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        # Retrieve all the Menu objects
        items = Menu.objects.all()
        
        # Check that we successfully created exactly 2 items in setUp
        self.assertEqual(len(items), 2)
        
        # Verify the string format of the first item matches what we expect
        self.assertEqual(str(items[0]), "IceCream : 80.00")
from django.test import TestCase
from .models import Order

# Create your tests here.
class CheckoutModelTest(TestCase):
    
    """
    Test for checkout
    """

    def test_checkout(self):
        checkout = Order(full_name = "test name", phone_number = "07070707070", country = "United Kingdom", postcode = "CO1 111", town_or_city = "London", street_address = "1 First Street", county = "Essex")
        self.assertEqual(checkout.full_name, "test name")
        self.assertEqual(checkout.phone_number, "07070707070")
        self.assertEqual(checkout.country, "United Kingdom")
        self.assertEqual(checkout.postcode, "CO1 111")
        self.assertEqual(checkout.town_or_city, "London")
        self.assertEqual(checkout.street_address, "1 First Street")
        self.assertEqual(checkout.county, "Essex")
        
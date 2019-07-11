from django.test import TestCase
from .models import Issue

# Create your tests here.
class IssueTests(TestCase):
    
    """
    Test for issue title
    """
    
    def test_str(self):
        test_name = Issue(title = "issue one")
        self.assertEqual(str(test_name), "issue one")
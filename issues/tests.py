from django.test import TestCase
from .models import Issue
from django.contrib.auth.models import User

# Create your tests here.
class IssueModelTest(TestCase):
    
    """
    Test for adding and issue
    """

    def test_issue(self):
        user = User()
        issue = Issue(title = "Test Issue Title", issue_type = "Feature", description = "Test Issue Description", requested_by = user, status = "Not Started", price = 99.99)
        self.assertEqual(issue.title, "Test Issue Title")
        self.assertEqual(issue.description, "Test Issue Description")
        self.assertEqual(issue.requested_by, user)
        self.assertEqual(issue.price, 99.99)
        self.assertEqual(issue.issue_type, "Feature")
        self.assertEqual(issue.status, "Not Started")
      
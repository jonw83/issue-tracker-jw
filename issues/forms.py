from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'description')
        
class EditIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'description', 'requested_by', 'date_created', 'status', 'completed_date')


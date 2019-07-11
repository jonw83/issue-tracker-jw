from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Issue
from .forms import IssueForm

# Create your views here.

@login_required()
def all_issues(request):
    issues = Issue.objects.all()
    return render(request, "issues.html", {"issues": issues})

@login_required()
def add_issue(request):
    if request.method == 'POST':
        issue_form = IssueForm(request.POST)
        
        if issue_form.is_valid():
            issue = issue_form.save(commit=False)
            issue.date = timezone.now()
            issue.save()
        
            return redirect(reverse('issues'))
        
        else:
            print(issue_form.errors)
            messages.error(request, "Please complete all fields")

    else:
        issue_form = IssueForm()
    
    return render(request, "addissue.html", {"issue_form": issue_form})

    
    
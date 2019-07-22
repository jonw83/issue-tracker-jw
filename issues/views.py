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

def add_issue(request):
    if request.method == 'POST':
        issue_form = IssueForm(request.POST)
        
        if issue_form.is_valid():
            issue = issue_form.save(commit=False)
            issue.date = timezone.now()
            issue.requested_by = request.user
            
            if issue.issue_type == 'Feature':
                issue.price = 99.99
                issue.save()
                
                cart = request.session.get('cart', {})
                issue_id = issue.pk
            
                cart[issue_id] = cart.get(issue_id, 1)
                request.session['cart'] = cart
                
            else:
                issue.price = 00.00
                issue.save()
            return redirect(reverse('issues'))
            
    else:
        issue_form = IssueForm()
        
    return render(request, 'addissue.html', {'issue_form': issue_form})
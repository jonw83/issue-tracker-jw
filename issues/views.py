from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Issue
from .forms import IssueForm, EditIssueForm

# Create your views here.

@login_required()
def all_issues(request):
    """Displays all issue requests"""
    issues = Issue.objects.all().order_by('-date_created')
    return render(request, "issues.html", {"issues": issues})
    
@login_required()
def add_issue(request):
    """Add issue to issue tracker"""
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
            
                return redirect(reverse('view_cart'))
                
            else:
                issue.price = 00.00
                issue.save()
            return redirect(reverse('issues'))
            
    else:
        issue_form = IssueForm()
        
    return render(request, 'addissue.html', {'issue_form': issue_form})

@login_required()
def edit_issue(request, pk):
    """Allow superuser to edit issue"""
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == 'POST':
        edit_issue_form = EditIssueForm(request.POST, request.FILES, instance=issue)            
        if edit_issue_form.is_valid():
            issue=edit_issue_form.save()
            return redirect(reverse('issues'))
    else:
        edit_issue_form = EditIssueForm(instance=issue)
        return render(request, 'editissue.html', {'edit_issue_form': edit_issue_form})
        
@login_required()
def upvote(request, pk):
    """Upvote an issue"""
    issue = Issue.objects.get(pk=pk)
    issue.upvotes += 1
    issue.save()
    messages.success(request, 'Thanks for the upvote!')
    return redirect('issues')
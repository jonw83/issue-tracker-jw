from django.conf.urls import url, include
from .views import all_issues, add_issue, edit_issue, upvote

urlpatterns = [
    url(r'^$', all_issues, name = 'issues'),
    url(r'^addissue/$', add_issue, name = 'addissue'),
    url(r'^(?P<pk>\d+)/editissue/$', edit_issue, name = 'editissue'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote, name='upvote'),
    ]





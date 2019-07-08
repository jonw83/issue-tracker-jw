from django.conf.urls import url, include
from .views import all_issues, add_issue

urlpatterns = [
    url(r'^$', all_issues, name = 'issues'),
    url(r'^addissue/$', add_issue, name = 'addissue'),
    ]





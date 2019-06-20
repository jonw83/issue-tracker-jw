from django.db import models
from django.utils import timezone

TYPE =  [
    ('Bug', 'Bug'),
    ('Feature', 'Feature') 
    ]
    
STATUS =  [
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'), 
    ('Complete', 'Complete')
    ]
    
# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=254, blank=False, default='')
    type = models.CharField(max_length=10, choices=TYPE, blank=False, default='Bug')
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=25, choices=STATUS, default='Not Started')
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    
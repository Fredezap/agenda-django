from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today, blank=True, null=True)
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
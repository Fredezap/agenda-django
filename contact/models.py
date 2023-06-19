from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    company = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
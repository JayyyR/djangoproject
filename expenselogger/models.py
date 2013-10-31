from django.db import models

class Expense(models.Model):
    TYPE_CHOICES = (
    ('FL', 'Flight'),
    ('CA', 'Car Rental'),
    ('HO', 'Hotel'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices= TYPE_CHOICES);
    amount = models.IntegerField(default=0)
    date = models.DateTimeField("Date")
    
    def __unicode__(self):
        return self.name
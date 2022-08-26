from django.db import models
from django.core.validators import RegexValidator

# validator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Choice for the type feild 
VEHICLE_TYPE = (
    ('two','TWO WHEELER'),
    ('three','THREE WHEELER'),
    ('four','FOUR WHEELER'),
)

class Vehicles(models.Model):
    ''' Vehicle data base table'''
    vehicle_number = models.CharField(max_length=50,validators=[alphanumeric])
    type  = models.CharField(max_length = 30,choices = VEHICLE_TYPE,default = 'CHOOSE')
    vehicle_model = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.vehicle_number
    
    
    
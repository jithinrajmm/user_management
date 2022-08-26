from pyexpat import model
from superadmin.models import Vehicles
from django.forms import ModelForm,Textarea


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'rows': 3}),
        
        }
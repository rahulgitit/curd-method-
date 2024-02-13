from django import forms 
from enroll.models import databaseintodolist

class tododataForm(forms.ModelForm):
    class Meta:
        model=databaseintodolist
        fields="__all__"
        
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "descriptions": forms.TextInput(attrs={'class':'form-control'}),
        }
        

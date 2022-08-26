from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Comments

class CommetsForm(forms.ModelForm):
    
    name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)
    rank = forms.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = Comments
        fields = ['name', 'last_name', 'rank', 'description']
        
    def __init__(self, *args, **kwargs):
        super(CommetsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Ingresa tu Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingresa tu Apellido'
        self.fields['rank'].widget.attrs['placeholder'] = 'Calificación 1-10'
        self.fields['description'].widget.attrs['placeholder'] = 'Deja tu Comentario'
        
    # def clean(self):
    #     cleaned_data = super(CommetsForm, self).clean()
        
from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('create_date',)
        widgets = {
            'date_end': DateInput(attrs={'type':'date'}),
        }
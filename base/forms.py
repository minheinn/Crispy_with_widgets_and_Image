from django import forms
from . models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'bio', 'age', 'image')
        widgets = {
            "name":forms.TextInput(attrs=({'placeholder':'Enter Your Name...', 'class':'form-control'})),
            "email":forms.EmailInput(attrs=({'placeholder':"Enter Your Email..."})),
            "bio":forms.Textarea(attrs=({'placeholder':"Enter Your Bio..."})),
            "age":forms.NumberInput(attrs=({'placeholder':"Enter Your Age..."})),
            'image':forms.FileInput(attrs=({"placeholder":"Image"})),
        }
from django import forms
from . import models


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            "first_name", 
            "last_name", 
            "date_of_birth", 
            "date_of_death"
        ]
        
class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            "name", 
            "author",
            "description"            
        ]
  
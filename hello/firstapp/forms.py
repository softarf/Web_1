
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")          # HTML: <input type="text">
    age = forms.IntegerField(label="Возраст клиента")    # HTML: <input type="number">

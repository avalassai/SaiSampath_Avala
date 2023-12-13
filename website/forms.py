from django.contrib.auth.models import User
from django import forms
from .models import Record



class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}) , label="Name")
    email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}) , label="Email")
    notes = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"", "class":"form-control",'rows':8}),label="Notes")


    class Meta:
        model = Record
        exclude = ("user",)
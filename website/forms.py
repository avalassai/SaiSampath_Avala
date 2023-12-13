from django.contrib.auth.models import User
from django import forms
from .models import Record



class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Enter Name", "class":"form-control"}) , label="")
    email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}) , label="")
    notes = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Notes", "class":"form-control",'rows':8}),label="")


    class Meta:
        model = Record
        exclude = ("user",)
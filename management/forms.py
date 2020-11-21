from django import forms
from django.forms import ModelForm
from .models import Employe, Managerr

class ManagerForm(forms.ModelForm):
    mobile = forms.IntegerField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Mobile Number"
        }))
    dob = forms.DateField(label=False,widget=forms.DateInput(
        attrs={
            'class': 'form-control datetimepicker-input p-2 my-2',
            'data-target': '#datetimepicker1',
            'placeholder': "Date of Birth : mm/dd/yyyy"
        }))

    company = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Company"
        }))

    city = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "City"
        }))

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-2 my-2",
                'type': "text",
                'placeholder': "Address",
                'rows':2
            }),
        label=False,
    )
    
    class Meta:
        model = Managerr
        fields = ('mobile', 'dob','city', 'address')


class EmployeForm(forms.ModelForm):
    empId = forms.CharField(max_length=20, label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Enter unique employee Id"
        }))
    firstname = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Employee First Name"
        }))
    lastname = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Employee Last Name"
        }))
    mobile = forms.IntegerField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "Mobile Number"
        }))
    dob = forms.DateField(label=False,widget=forms.DateInput(
        attrs={
            'class': 'form-control datetimepicker-input p-2 my-2',
            'data-target': '#datetimepicker1',
            'placeholder': "Date of Birth : mm/dd/yyyy"
        }))

    city = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control p-2 my-2",
            'type': "text",
            'placeholder': "City"
        }))

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-2 my-2",
                'type': "text",
                'placeholder': "Address",
                'rows':2
            }),
        label=False,
    )
    
    class Meta:
        model = Employe
        fields = ('empId','firstname', 'lastname','mobile', 'dob','city', 'address')

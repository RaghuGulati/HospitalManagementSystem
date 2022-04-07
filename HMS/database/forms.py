from django import forms
from .models import *
import pytz
from django.forms import ModelChoiceField

class register_form(forms.Form):
    fname = forms.CharField(
                    widget=forms.TextInput(
                    attrs={ "class": " ",
                        "placeholder": "Enter First Name",
                        }
                    ),
                    required=True,
                    max_length=50,
                    label = "First Name"
            )
    lname = forms.CharField(
                    widget=forms.TextInput(
                    attrs={ "class": " ",
                        "placeholder": "Enter Last Name",
                        }
                    ),
                    required=True,
                    max_length=50,
                    label = "Last Name"
        )   

    uname = forms.CharField(
                    widget=forms.TextInput(
                    attrs={ "class": " ",
                        "placeholder": "Create username",
                        }
                    ),
                    required=True,
                    max_length=50,
                    label = "Username"
        )    

    email = forms.CharField(
                    widget=forms.EmailInput(
                    attrs={"class": " ",  "placeholder": "Enter Email Id"}),
                    required=True,
                    label = "Email Id"       
                    )


    password = forms.CharField(
                    widget=forms.PasswordInput(
                    attrs={"class": " ",  "placeholder": "Enter Password"}),
                    required=True,
                    max_length=8,
                    )

    conf_password = forms.CharField(
                    widget=forms.PasswordInput(
                    attrs={"class": " ",  "placeholder": "Confirm Password"}),
                    required=True,
                    max_length=8,
                    )

    mobile = forms.CharField(widget=forms.TextInput(
                    attrs={ "placeholder": "Mobile Number",
                        }
                    ),
                    required=True,
                    label = "Mobile Number",
    )

    age = forms.CharField(widget=forms.NumberInput(
                    attrs={ "placeholder": "Age",
                        }
                    ),
                    required=True,
                    label = "Age",
    )


class register2(forms.Form):
    gender_choices = [('Male','Male'),('Female','Female')]

    gender = forms.ChoiceField(
                        choices = gender_choices,
                        widget=forms.RadioSelect(
                                attrs ={
                                        'id':'myid',
                                }
                                ),
                        label = 'Gender'
                    )

    register_choices = [('Doctor','Doctor'),('Patient','Patient')]

    registerf = forms.ChoiceField(
                        choices = register_choices,
                        widget=forms.RadioSelect(
                                attrs ={
                                        'id':'myid',
                                }
                                ),
                        label = 'Register as'
                    )

class login_form(forms.Form):
    uname = forms.CharField(
                    widget=forms.TextInput(
                    attrs={ "class": "form-control",
                        "placeholder": "Enter username",
                        }
                    ),
                    required=True,
                    max_length=50,
                    label = "Username"
        )    
    email = forms.CharField(
                    widget=forms.EmailInput(
                    attrs={"class": "form-control",  "placeholder": "Enter Email Id"}),
                    required=True,
                    label = "Email Id"       
                    )


    password = forms.CharField(
                    widget=forms.PasswordInput(
                    attrs={"class": "form-control",  "placeholder": "Enter Password"}),
                    required=True,
                    max_length=8,
                    )

    register_choices = [('doctor','doctor'),('patient','patient'),('hr','hr'),('receptionist', 'receptionist')]

    registerf = forms.ChoiceField(
                        choices = register_choices,
                        widget=forms.RadioSelect(
                                attrs ={
                                        'id':'myid',
                                }
                                ),
                        label = 'Register as'
                    )


class upload_medical_report(forms.Form):
     medical_report = forms.FileField()

class app_recommend_form(forms.Form):
    appid = forms.ChoiceField()
    drid = forms.ChoiceField()
    #datetime = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        b = appointments.objects.filter(status = 'request queued').values_list('id', flat = True).distinct()
        c = doctor.objects.values_list('name', flat = True).distinct()
        choices = [(i,i) for i in b]     
        choices2 = [(j,j) for j in c]    
        
        self.fields['appid'].choices = choices
        self.fields['drid'].choices = choices2

class doctormodelform(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['status', 'salary']

class prescriptionmodelform(forms.ModelForm):
    class Meta:
        model = prescriptions
        fields = ['other_fees']


    

    #def 
    '''
    appid = forms.ModelChoiceField(queryset = appointments.objects.filter(status = 'request queued').values_list('id', flat = True).distinct())
    drid = forms.ModelChoiceField(queryset = doctor.objects.all().values_list('name', flat = True).distinct())
    datetime = forms.DateTimeField()
    '''

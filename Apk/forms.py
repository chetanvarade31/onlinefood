
from email.errors import HeaderParseError
from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import TextInput

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','Placeholder': 'Enter Password'}),label="Password")
    password2 = forms.CharField(label="Password Confirmation",widget= forms.PasswordInput(attrs={'class':'form-control','Placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ["username",'email']
        labels = {"email":"Email"}
        

        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control', 'Placeholder' : 'Enter Username' }),
            'email' : forms.EmailInput(attrs = {'class' : 'form-control','Placeholder': 'Enter Email'}),
            
        }

class SignInform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','Placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','Placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username','password']
        

        
class UserInfo(forms.Form):

    Name = forms.CharField(required=True,widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter Your Full Name'}))
    Mobile = forms.IntegerField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Enter Your Mobile Number'}))
    Address = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Full Address Here'}))
    City = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'City'}))
    District = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'District'}))
    State = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Enter here state'}))
    Gender = forms.ChoiceField(widget=forms.Select(attrs= {'class':'form-control'}),choices=[('Male','Male'),('Female','Female')])
    Zipcode = forms.IntegerField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Enter Zipcode here '}))
  
class TableForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Full Name'}))
    persons = forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control','Placeholder':'Number of Persons'}),min_value=1,max_value=6)
    tables = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','Placeholder':'Number of Tables Want'}),min_value=1)
    date = forms.DateField(widget= forms.DateInput(attrs= {'class':'form-control','Placeholder':'Date of Booking','type':'date'}))
    time = forms.TimeField(widget= forms.TimeInput(attrs= {'class':'form-control','Placeholder':'Time on Booking Date','type':'time'}))
    mobile = forms.IntegerField(widget= forms.NumberInput(attrs= {'class':'form-control','Placeholder':'Mobile Number'}))


class ReviewForm(forms.Form):
    message = forms.CharField(widget= forms.Textarea(attrs= {'class':'form-control','Placeholder':'Type Here !!'}))
    

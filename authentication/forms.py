from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Contact_Person





class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your First Name'}))
    last_name = forms.CharField(max_length=100,label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Last Name'}))
    email = forms.EmailField(max_length=200,label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your Email'}), help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Your Username'})
        self.fields['username'].label=""
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Your Password'})
        self.fields['password1'].label=""
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['password2'].label=""

# Options = [
#         ('1', 'Hello'),
#         ('2', 'World'),
#       ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = ('designation','contact')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm,self).__init__(*args, **kwargs)

        self.fields['designation'].widget.attrs.update({'class': 'form-control'})
        self.fields['designation'].widget.attrs.update({'placeholder': 'Enter Your Designation'})
        self.fields['designation'].label=""
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'Enter Your Phone Number. eg 0204559834'})
        self.fields['contact'].label=""




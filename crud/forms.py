from django.forms import ModelForm
from django import forms
from authentication.models import Institution, Business_Details, Management, Institution_Type, Institution_Head, Accreditation
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput




class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'
        exclude = ['user','status','type']
        labels = {
           'name': 'Name of Institution',
            'postal_address': 'Postal Address',
            'digital_address': 'Digital Address',
            'town': 'Town/City',
            'email': 'Email of Institution',
            'website': 'Website',
            'contact': 'Official Phone Number',
            'establishment_date': 'Date of Establishment',
        }
        widgets = {
            # 'establishment_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'establishment_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

    
    def __init__(self, *args, **kwargs):
        super(InstitutionForm,self).__init__(*args,**kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Name of Institution'})

        self.fields['postal_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['postal_address'].widget.attrs.update({'placeholder': 'Postal Address'})

        self.fields['digital_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['digital_address'].widget.attrs.update({'placeholder': 'Digital Address'})

        self.fields['town'].widget.attrs.update({'class': 'form-control'})
        self.fields['town'].widget.attrs.update({'placeholder': 'Town/City'})

        self.fields['region'].widget.attrs.update({'class': 'form-control'})
        self.fields['region'].widget.attrs.update({'placeholder': 'Please select'})

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email of Institution'})

        self.fields['website'].widget.attrs.update({'placeholder': 'Website'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})

        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'g. 0207889837'})

        self.fields['establishment_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['establishment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})




class businessDetailsForm(forms.ModelForm):
    class Meta:
        model = Business_Details
        fields = '__all__'
        exclude = ['user']
        labels = {
            'registration_date': 'Date of Registration',
            'agency_name': 'Agency Name',
            'registration_number': 'Registration Number',
            'agency_type' : 'Bussiness Registration Type'
        }
        widgets = {
            # 'registration_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'registration_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


    
    def __init__(self, *args, **kwargs):
        super(businessDetailsForm,self).__init__(*args,**kwargs)

        self.fields['registration_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['registration_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})


        self.fields['agency_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['agency_name'].widget.attrs.update({'placeholder': 'Agency Name'})

        self.fields['registration_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['registration_number'].widget.attrs.update({'placeholder': 'Registration Number'})

        self.fields['agency_type'].widget.attrs.update({'class': 'form-control','onchange': 'myBusinessFunction()'})





class managementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'
        exclude = ['user','type']
        labels = {
            'appointment_date': 'Date of Appointment',
        }
        widgets = {
            # 'registration_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'appointment_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


    
    def __init__(self, *args, **kwargs):
        super(managementForm,self).__init__(*args,**kwargs)

        self.fields['appointment_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['appointment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})

        self.fields['designation'].widget.attrs.update({'class': 'form-control'})
        # self.fields['appointment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'eg. samfox@gmail.com'})

        self.fields['official_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['official_contact'].widget.attrs.update({'placeholder': 'eg. 0307889837'})

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Name of Registrar'})

        self.fields['personal_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['personal_contact'].widget.attrs.update({'placeholder': 'eg. 0207889837'})





class InstitutionHeadForm(forms.ModelForm):
    class Meta:

        model = Institution_Head
        fields = '__all__'
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super(InstitutionHeadForm,self).__init__(*args,**kwargs)

        self.fields['designation'].widget.attrs.update({'class': 'form-control'})
        # self.fields['appointment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Name of head of Institution'})

        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'eg. 0205448723'})

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email'})





class AccreditationForm(forms.ModelForm):
    class Meta:

        model = Accreditation
        fields = '__all__'
        exclude = ['user']

    choices = [
        ('Yes','Yes'),
        ('No','No')
    ]

    status = forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect())


    def __init__(self, *args, **kwargs):
        super(AccreditationForm,self).__init__(*args,**kwargs)

        # self.fields['status'].widget.attrs.update({'class': 'form-control'})



# class InstitutionForm(forms.ModelForm):
#     class Meta:
#         model = Institution
#         fields = '__all__'
#         exclude = ['user','status','type']
#         labels = {
#             'name': 'Name of Institution',
#             'postal_address': 'Postal Address',
#             'digital_address': 'Digital Address',
#             'town': 'Town/City',
#             'email': 'Email of Institution',
#             'website': 'Website',
#             'contact': 'Official Phone Number',
#             'establishment_date': 'Date of Establishment',
#         }


    
#     def __init__(self, *args, **kwargs):
#         super(InstitutionForm,self).__init__(*args,**kwargs)
#         self.fields['name'].widget.attrs.update({'class': 'form-control'})
#         self.fields['name'].widget.attrs.update({'placeholder': 'Name of Institution'})

#         self.fields['postal_address'].widget.attrs.update({'class': 'form-control'})
#         self.fields['postal_address'].widget.attrs.update({'placeholder': 'Postal Address'})

#         self.fields['digital_address'].widget.attrs.update({'class': 'form-control'})
#         self.fields['digital_address'].widget.attrs.update({'placeholder': 'Digital Address'})

#         self.fields['town'].widget.attrs.update({'class': 'form-control'})
#         self.fields['town'].widget.attrs.update({'placeholder': 'Town/City'})

#         self.fields['email'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].widget.attrs.update({'placeholder': 'Email of Institution'})


#         self.fields['website'].widget.attrs.update({'placeholder': 'Website'})
#         self.fields['website'].widget.attrs.update({'class': 'form-control'})

#         self.fields['contact'].widget.attrs.update({'class': 'form-control'})
#         self.fields['contact'].widget.attrs.update({'placeholder': 'Official Phone Number'})

#         self.fields['establishment_date'].widget.attrs.update({'class': 'form-control'})
#         self.fields['establishment_date'].widget.attrs.update({'placeholder': 'Date of Establishment'})







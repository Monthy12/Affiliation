from django.forms import ModelForm
from django import forms
from authentication.models import Institution, Business_Details, Management
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput




class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        
        fields = ['establishment_date',]
        labels = {
            'establishment_date': 'Date of Establishment',
        }
        widgets = {
            # 'establishment_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'establishment_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


    
    def __init__(self, *args, **kwargs):
        super(InstitutionForm,self).__init__(*args,**kwargs)

        self.fields['establishment_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['establishment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})




class businessDetailsForm(forms.ModelForm):
    class Meta:
        model = Business_Details
        fields = ['registration_date',]
        labels = {
            'registration_date': 'Date of Registration',
        }
        widgets = {
            # 'registration_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'registration_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


    
    def __init__(self, *args, **kwargs):
        super(businessDetailsForm,self).__init__(*args,**kwargs)

        self.fields['registration_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['registration_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})



class managementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['appointment_date',]
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







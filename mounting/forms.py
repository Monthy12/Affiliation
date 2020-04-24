from django.forms import ModelForm
from django import forms
from authentication.models import Department
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput




class departmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ['user','status']
        labels = {
            'appointment_date': 'Date of Appointment',
        }
        widgets = {
            # 'establishment_date': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
            'appointment_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


    
    def __init__(self, *args, **kwargs):
        super(departmentForm,self).__init__(*args,**kwargs)

        self.fields['appointment_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['appointment_date'].widget.attrs.update({'placeholder': 'yyyy-mm-dd'})

        self.fields['department_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['department_name'].widget.attrs.update({'placeholder': 'Department Name'})

        self.fields['name_department_head'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_department_head'].widget.attrs.update({'placeholder': 'Name of Department Head'})

        self.fields['highest_qualification'].widget.attrs.update({'class': 'form-control'})
        self.fields['highest_qualification'].widget.attrs.update({'placeholder': 'Highest Qualifications'})

        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'eg. 0205669834'})

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'eg. kule12@gmail.com'})
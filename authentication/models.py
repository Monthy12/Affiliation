from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
# from multiselectedfield import MultiSelectedField





class Institution(models.Model):

    class Meta:
        db_table = 'Institution'

    REGION = (
        ("Bono East Region","Bono East Region"),
        ("Ahafo Region","Ahafo Region"),
        ("Bono Region","Bono Region"),
        ("North East Region","North East Region"),
        ("Savannah Region","Savannah Region"),
        ("Western North Region","Western North Region"),
        ("Western Region","Western Region"),
        ("Volta Region","Volta Region"),
        ("Greater Accra Region","Greater Accra Region"),
        ("Eastern Region","Eastern Region"),
        ("Ashanti Region","Ashanti Region"),
        ("Central Region","Central Region"),
        ("Northern Region","Northern Region"),
        ("Upper East Region","Upper East Region"),
        ("Upper West Region","Upper West Region"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    postal_address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    website = models.CharField(max_length=100,null=True)
    town = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True,choices=REGION)
    digital_address = models.CharField(max_length=50,null=True)
    establishment_date =  models.DateField(null=True,auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50,null=True,default='incomplete')
    type = models.CharField(max_length=50,null=True,default="affiliation")

    # def __str__(self):
    #     return self.name





class Institution_Head(models.Model):

    class Meta:
        db_table = 'Institution_Head'

    DESIGNATION = (
        ("Mr","Mr"),
        ("Mrs","Mrs"),
        ("Miss","Miss"),
        ("Dr","Dr"),
        ("Prof","Prof"),
        ("Rev","Rev"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50,choices=DESIGNATION, null=True)
    name = models.CharField(max_length=300, null=True)
    contact = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)



class Contact_Person(models.Model):

    class Meta:
        db_table = 'Contact_Person' 

    DESIGNATION = (
        ("Mr","Mr"),
        ("Mrs","Mrs"),
        ("Miss","Miss"),
        ("Dr","Dr"),
        ("Prof","Prof"),
        ("Rev","Rev"),
    )
    
    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    designation  = models.CharField(max_length=50, choices=DESIGNATION)
    contact  = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.contact




class Department(models.Model):

    class Meta:
        db_table = 'Department'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100,null=True)
    name_department_head = models.CharField(max_length=100, null=True)
    highest_qualification = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
    status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.contact



# class Management(models.Model):

#     class Meta:
#         db_table = 'Management'
    
#     institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
#     designation = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     other_name = models.CharField(max_length=50)
#     degree = models.CharField(max_length=100)
#     programme_area = models.CharField(max_length=100)
#     awarding_institution = models.CharField(max_length=100)
#     completion_year = models.PositiveSmallIntegerField()
#     appointment_year = models.PositiveSmallIntegerField()



class Library_Books(models.Model):

    class Meta:
        db_table = 'Library_Books'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    subject_area = models.CharField(max_length=100,null=True)
    book_number = models.CharField(max_length=100,null=True)
    book_reference =models.CharField(max_length=100,null=True) 
    ebook_number = models.CharField(max_length=100,null=True)
    audio_visual = models.CharField(max_length=100,null=True)
    others = models.CharField(max_length=100,null=True)



class Laboratory(models.Model):

    class Meta:
        db_table = 'Laboratory'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    lab_type = models.CharField(max_length=100,null=True)
    fixed_item = models.CharField(max_length=100,null=True)
    quantity_of_fixed_item = models.CharField(max_length=100,null=True)
    consummable = models.CharField(max_length=100,null=True)
    quantity_of_consummable =models.CharField(max_length=100,null=True) 




class Lecture_Room(models.Model):

    class Meta:
        db_table = 'Lecture_Room'
    
    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100,null=True)



class Facility(models.Model):

    class Meta:
        db_table = 'Facility'
    
    # facility = models.ForeignKey('Lecture_Room', on_delete=models.CASCADE)
    item_list = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)



class Programme(models.Model):

    class Meta:
        db_table = 'Programme'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    programme_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default = 'pending')
    inst_name = models.CharField(max_length=50, default = 'test')

    def __str__(self):
        return self.status




class Affiliation(models.Model):

    class Meta:
        db_table = 'Affiliation'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    affiliate_name = models.CharField(max_length=100,default='test')
    # affiliate_programme = models.CharField(max_length=100, default='test')
    # affiliate_level = models.CharField(max_length=50, default='test')

    def __str__(self):
        return self.affiliate_name




class Mentor(models.Model):

    class Meta:
        db_table = 'Mentor'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    mentor_name = models.CharField(max_length=100,default='test')
    mentor_programme = models.CharField(max_length=100, default='test')
    mentor_level = models.CharField(max_length=50, default='test')

    def __str__(self):
        return self.mentor_name



class Examination_Unit(models.Model):

    class Meta:
        db_table = 'Examination_Unit'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100,null=True)




class Institution_Type(models.Model):

    class Meta:
        db_table = 'Institution_Type'

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    type = models.CharField(max_length=100,default='test', null=True)







class Business_Details(models.Model):

    class Meta:
        db_table = 'Business_Details'

    choices = (
        ("RGD","Registrar General Department"),
        ("MMDA","Metropolitan, Municipal and District Assemblies"),
        ("Professional Agency","Professional Agency"),
    )

    # institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    agency_type = models.CharField(max_length=100,null=True, choices = choices)
    agency_name = models.CharField(max_length=200,null=True)
    registration_date = models.DateField(null=True)
    registration_number = models.CharField(max_length=100,null=True)



class Document(models.Model):

    class Meta:
        db_table = 'Document'
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    title = models.CharField(max_length=300, default="document")
    type = models.CharField(max_length=300, default="document")
    document = models.FileField(upload_to='documents')
    datetime = models.DateField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title



class Payment(models.Model):

    class Meta:
        db_table = 'Payment'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default="payment")
    payment = models.FileField(upload_to='payments')
    datetime = models.DateField(auto_now=True)
    
    def delete(self, *args, **kwargs):
        self.payment.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title



class test_data(models.Model):

    class Meta:
        db_table = 'test_data'

    name = models.CharField(max_length=50, null=True)



class Management(models.Model):

    class Meta:
        db_table = 'Management'

    DESIGNATION = (
        ("Mr","Mr"),
        ("Mrs","Mrs"),
        ("Miss","Miss"),
        ("Dr","Dr"),
        ("Prof","Prof"),
        ("Rev","Rev"),
    )

    
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, default = 'test')
    type = models.CharField(max_length=50, null=True, default = 'test')
    designation = models.CharField(max_length=50,null=True, choices = DESIGNATION)
    appointment_date = models.DateField(null=True,auto_now=False, auto_now_add=False)
    personal_contact = models.CharField(max_length=100, null=True, default = 'test')
    official_contact = models.CharField(max_length=100, null=True, default = 'test')
    email = models.CharField(max_length=100, null=True, default = 'test')
    # completion_year = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name



class Status(models.Model):

    class Meta:
        db_table = 'Status'

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=True, default = 'test')
    status = models.CharField(max_length=50, null=True, default = 'test')

    def __str__(self):
        return self.status



class Accreditation(models.Model):

    class Meta:
        db_table = 'Accreditation'

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=True, default = 'test')


    def __str__(self):
        return self.status


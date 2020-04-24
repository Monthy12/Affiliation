from django.shortcuts import render,redirect, Http404, get_object_or_404
from authentication.models import Institution, Institution_Type, Business_Details, Affiliation, Examination_Unit, Laboratory, Library_Books, Facility, Lecture_Room, Institution_Head, Document, Payment, Management, Status, Contact_Person, Accreditation, Programme, Department
from django.utils import six 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from authentication.functions import sendSms
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import InstitutionForm, businessDetailsForm, managementForm, InstitutionHeadForm, AccreditationForm
from mounting.forms import departmentForm

# Create your views here.

@login_required(login_url="/authenticate/login")
def institution(request):

    if request.method == 'POST':

        form = InstitutionForm(request.POST)

        if form.is_valid():

            if Institution.objects.filter(user = request.user).count():
                institutionObject = Institution.objects.get(user = request.user)
                institutionEditObject = InstitutionForm(request.POST or None, instance = institutionObject)
                institutionEditObject.user = request.user
                institutionEditObject.save()

                print(institutionEditObject)

            else:
                    
                institutionInstance = form.save(commit=False)
                institutionInstance.user = request.user
                institutionInstance.save()       


        return redirect('institution_type')



    else:
        institutionObject = Institution.objects.get(user = request.user)
        # institutionHeadObject = Institution_Head.objects.get(user = request.user)

        # registrationDate = businessDetailsForm()
        institution_instance = InstitutionForm(instance = institutionObject)
        # institutionHead_instance = InstitutionHeadForm(instance = institutionHeadObject)
        context = {'form':institution_instance}
        return render(request,'crud/institution1.html',context)



@login_required(login_url="/authenticate/login")
def institution_type(request):

    if request.method == 'POST':

        if Institution_Type.objects.filter(user = request.user).count():
            institutionTypeObject =  Institution_Type.objects.filter(user = request.user)
            institutionTypeObject.delete()


            institution_type_item = request.POST
            item = dict(six.iterlists(institution_type_item))

            for inst_type_item in item['inst_type']:

                inst_type_instance = Institution_Type(type=inst_type_item)
                inst_type_instance.user = request.user
                inst_type_instance.save()

                return redirect('institution_head')

        else:

            institution_type_item = request.POST
            item = dict(six.iterlists(institution_type_item))

            for inst_type_item in item['inst_type']:

                inst_type_instance = Institution_Type(type=inst_type_item)
                inst_type_instance.user = request.user
                inst_type_instance.save()

                return redirect('institution_head')

    else:

        return render(request,'crud/institution_type.html')




@login_required(login_url="/authenticate/login")
def institution_head(request):

    if request.method == 'POST':

        headInstForm = InstitutionHeadForm(request.POST)
        # print(headInstForm)

        if headInstForm.is_valid():

            item = Institution_Head.objects.filter(user = request.user).count()

            if item:
                # print(item)
                
                institutionHeadObject = Institution_Head.objects.get(user = request.user)
                institutionHeadEditObject = InstitutionHeadForm(request.POST or None, instance = institutionHeadObject)
                institutionHeadEditObject.user = request.user
                institutionHeadEditObject.save()


            else:
                
                institutionHeadInstance = headInstForm.save(commit=False)
                institutionHeadInstance.user = request.user
                institutionHeadInstance.save()

        return redirect('bussiness_registeration')

    else:

        institutionHeadObject = Institution_Head.objects.get(user = request.user)
        institutionHead_instance = InstitutionHeadForm(instance = institutionHeadObject)
        context = {'institutionHead_instance':institutionHead_instance}
    
        return render(request,'crud/institution_head.html',context)
    


@login_required(login_url="/authenticate/login")
def bussiness_registeration(request):

    if request.method == 'POST':
        
        bussiness_form = businessDetailsForm(request.POST)

        if bussiness_form.is_valid():
            
            item = Business_Details.objects.filter(user = request.user).count()

            if item:
                
                bussiness_registrationObject = Business_Details.objects.get(user = request.user)
                bussinessEditObject = businessDetailsForm(request.POST or None, instance = bussiness_registrationObject)
                bussinessEditObject.user = request.user
                bussinessEditObject.save()


            else:
                
                bussinessInstance = bussiness_form.save(commit=False)
                bussinessInstance.user = request.user
                bussinessInstance.save()

        return redirect('management_registrar')



    else:

        Business_DetailsObject = Business_Details.objects.get(user = request.user)
        businessDetailsForm_instance = businessDetailsForm(instance = Business_DetailsObject)
        context = {'form':businessDetailsForm_instance}
        return render(request,'crud/bussiness_details.html',context)




@login_required(login_url="/authenticate/login")
def management_registrar(request):

    if request.method == 'POST':

        management_registrarForm = managementForm(request.POST)

        if management_registrarForm.is_valid():

            management_registrarFormObject = Management.objects.filter(user = request.user,type='registrar')
 
            if management_registrarFormObject:
                management_registrarFormObject.delete()

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'registrar'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()


            else:

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'registrar'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()

        return redirect('management_finance')


    else:
        ManagementObject = Management.objects.get(user = request.user,type='registrar')

        ManagementForm = managementForm(instance = ManagementObject)
        context = {'form':ManagementForm}
        return render(request,'crud/management_registrar.html', context)



@login_required(login_url="/authenticate/login")
def management_finance(request):
    if request.method == 'POST':

        management_registrarForm = managementForm(request.POST)

        if management_registrarForm.is_valid():

            management_registrarFormObject = Management.objects.get(user = request.user,type='finance')
 
            if management_registrarFormObject:
                management_registrarFormObject.delete()

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'finance'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()


            else:

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'finance'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()


        return redirect('management_exam_officer')


    else:
        ManagementObject = Management.objects.get(user = request.user,type='finance')

        ManagementForm = managementForm(instance = ManagementObject)
        context = {'form':ManagementForm}
        return render(request,'crud/management_finance.html', context)



@login_required(login_url="/authenticate/login")
def management_exam_officer(request):

    if request.method == 'POST':

        management_registrarForm = managementForm(request.POST)

        if management_registrarForm.is_valid():

            management_registrarFormObject = Management.objects.get(user = request.user,type='examiner')
 
            if management_registrarFormObject:
                management_registrarFormObject.delete()

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'examiner'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()


            else:

                registrar_name = request.POST['name']
                registrar_designation = request.POST['designation']
                personal_contact = request.POST['personal_contact']
                official_contact = request.POST['official_contact']
                email = request.POST['email']
                re_appointment_date = request.POST['appointment_date']
                registrar_type = 'examiner'

                registrar_instance = Management(designation=registrar_designation,personal_contact=personal_contact,email=email,name=registrar_name,official_contact=official_contact,type=registrar_type,appointment_date=re_appointment_date)
                registrar_instance.user = request.user
                registrar_instance.save()


        return redirect('affiliate')


    else:
        ManagementObject = Management.objects.get(user = request.user,type='examiner')

        ManagementForm = managementForm(instance = ManagementObject)
        context = {'form':ManagementForm}
        return render(request,'crud/management_exam_officer.html', context)



@login_required(login_url="/authenticate/login")
def affiliation_programme_mount(request):
    if request.method == 'POST':

        level = request.POST['level']
        programme = request.POST['programme']
        inst_name = Institution.objects.get(user_id=request.user)


        programme_instance = Programme(level=level,programme_name=programme,status="incomplete",inst_name=inst_name)
        programme_instance.user = request.user
        # programme_instance.save()
    
        return redirect("affiliation_programme_department_head")

    else:

        return render(request,'crud/affiliate_programme.html')




@login_required(login_url="/authenticate/login")
def affiliation_programme_department_head(request):

    if request.method == 'POST':

        departmentFormInstance = departmentForm(request.POST)

        print(departmentFormInstance)

        if departmentFormInstance.is_valid():

            item = Department.objects.filter(user = request.user, status = '0').count()

            if item:
                print(item)
                
                departmentObject = Department.objects.get(user = request.user, status = '0')
                print(departmentObject)
                dept_head_instance = departmentForm(request.POST or None, instance = departmentObject)
                print(dept_head_instance)
                dept_head_instance.user = request.user
                dept_head_instance.save()


            else:

                dept_head_instance = departmentFormInstance.save(commit=False)
                dept_head_instance.user = request.user
                dept_head_instance.save()

            return redirect('affiliation_programme_details_of_room')

    else:
        departmentObject = Department.objects.get(user = request.user,status = '0')
        print(departmentObject)
        departmentHead = departmentForm(instance = departmentObject)
        context = {'form':departmentHead}
        return render(request, 'crud/affiliate_programme_department.html',context)




@login_required(login_url="/authenticate/login")
def affiliation_programme_details_of_room(request):

    if request.method == 'POST':

        room_dimension = request.POST['room_dimension']
        room_type = request.POST['room_type']

        
        room_instance = Lecture_Room(size=room_dimension, room_type=room_type)
        room_instance.user = request.user
        # room_instance.save()


        data = request.POST
        item = dict(six.iterlists(data))

        for itemValue in item['facility']:

            facility_instance = Facility(item_list=itemValue)
            facility_instance.user = request.user
            # facility_instance.save()

        return redirect('affiliation_programme_library')

    return render(request,'crud/affiliate_room_details.html')




@login_required(login_url="/authenticate/login")
def affiliation_programme_library(request):

    if request.method == 'POST':

        data = request.POST
        item = dict(six.iterlists(data))

        # print(item)
        itemCount = len(item['subject'])

        for itemList in range(itemCount):
            subject = item['subject'][itemList]
            number_of_books = item['number_of_books'][itemList]
            number_of_reference = item['number_of_reference'][itemList]
            number_of_ebooks = item['number_of_ebooks'][itemList]
            number_of_audio_visuals = item['number_of_audio_visuals'][itemList]
            number_of_others = item['number_of_others'][itemList]

            library_instance = Library_Books(subject_area=subject,book_number=number_of_books,book_reference=number_of_reference,ebook_number=number_of_ebooks,audio_visual=number_of_audio_visuals,others=number_of_others)
            library_instance.user = request.user
            # library_instance.save()


        return redirect('affiliation_programme_laboratory')

    else:
        return render(request, 'crud/affiliate_library.html')



@login_required(login_url="/authenticate/login")
def affiliation_programme_laboratory(request):

    if request.method == 'POST':

        data = request.POST
        item = dict(six.iterlists(data))

        # print(item)
        itemCount = len(item['lab_type'])

        for itemList in range(itemCount):
            lab_type = item['lab_type'][itemList]
            fixed_item = item['fixed_item'][itemList]
            quantity_of_fixed_item = item['quantity_of_fixed_item'][itemList]
            consummable = item['consummable'][itemList]
            quantity_of_consummable = item['quantity_of_consummable'][itemList]


            laboratory_instance = Laboratory(lab_type=lab_type,fixed_item=fixed_item,quantity_of_fixed_item=quantity_of_fixed_item,consummable=consummable,quantity_of_consummable=quantity_of_consummable)
            laboratory_instance.user = request.user
            # laboratory_instance.save()


        return redirect('affiliation_programme_exam_unit')

    else:
        
        return render(request,'crud/affiliate_laboratory.html')



@login_required(login_url="/authenticate/login")
def affiliation_programme_exam_unit(request):

    if request.method == 'POST':
        itemLists = {'itemList': ['Computers','Printers','UPS','Backup System','Cabinets','Reprographic Machines','Safes','Workiing Desk']}

        data = request.POST
        item = dict(six.iterlists(data))

        # print(item)
        itemCount = len(item['exam_quantity'])

        for itemList in range(itemCount):

            exam_instance = Examination_Unit(item=itemLists['itemList'][itemList],quantity=item['exam_quantity'][itemList])
            exam_instance.user = request.user
            # exam_instance.save()



        return redirect('affiliate')

    else:
        return render(request,'crud/affiliate_examination_unit.html')


@login_required(login_url="/authenticate/login")
def affiliate(request):

    if request.method == 'POST':

        accreditationForm = AccreditationForm(request.POST)

        # print(accreditationForm)
        if accreditationForm.is_valid():

            accreditationFormObject = Accreditation.objects.get(user = request.user)

            print(accreditationFormObject)

            # item = Institution_Head.objects.filter(user = request.user).count()

            if accreditationFormObject:
                # print(item)
            
                accreditationEditObject = AccreditationForm(request.POST or None, instance = accreditationFormObject)
                accreditationEditObject.user = request.user
                accreditationEditObject.save()


            else:
                
                accreditationInstance = accreditationForm.save(commit=False)
                accreditationInstance.user = request.user
                accreditationInstance.save()


        return redirect('affiliate')

    else:

        accreditationObject = Accreditation.objects.get(user = request.user)

        ManagementForm = AccreditationForm(instance = accreditationObject)
        context = {'form':ManagementForm}

        return render(request,'crud/affiliate.html', context)

    # if request.method == 'POST':



    #     status = request.POST['inst_accreditation']

    #     accreditation_instance = Accreditation(status=status)
    #     accreditation_instance.user = request.user
    #     accreditation_instance.save()

    #     return redirect('document_upload')

    # else:
    #     return render(request,'crud/affiliate.html', {})



@login_required(login_url="/authenticate/login")
def document_upload(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['doc_upload']
        documents_name = request.POST['documents_name']
        documents_name_referred = request.POST['doc_name']
        document_type = "affiliation document"


        if documents_name == 'referred':
            documents_name = documents_name_referred

        document_instance = Document(title = documents_name,document = uploaded_file,type=document_type)

        document_instance.user = request.user
        document_instance.save()

        
        return redirect('document_upload')

    document = Document.objects.filter(user_id=request.user,type="affiliation document")
    print(document)
    # document = Document.objects.all()
    return render(request, 'crud/document_upload.html',{'documents':document})



@login_required(login_url="/authenticate/login")
def delete_document(request, pk):

    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('document_upload')


@login_required(login_url="/authenticate/login")
def affiliate_payment(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['payment_upload']
        payment_name = request.POST['payment_name']

        payment_instance = Payment(type = payment_name, payment = uploaded_file)

        payment_instance.user = request.user
        payment_instance.save()

    payment_list = Payment.objects.filter(user_id=request.user,type="affiliation_payment")

    return render(request, 'crud/affiliate_payment.html',{'payments':payment_list})


@login_required(login_url="/authenticate/login")
def delete_payment(request, pk):

    if request.method == 'POST':
        payment = Payment.objects.get(pk=pk)
        payment.delete()

    return redirect('affiliate_payment')


@login_required(login_url="/authenticate/login")
def summary(request):

    # institutionSummary = Institution.objects.all()
    institutionSummary = Institution.objects.filter(user_id=request.user)
    institutionTypeSummary = Institution_Type.objects.filter(user_id=request.user)
    institutionHeadSummary = Institution_Head.objects.filter(user_id=request.user)
    businessDetailSummary = Business_Details.objects.filter(user_id=request.user)

    registrarSummary = Management.objects.filter(type='registrar',user_id=request.user)
    financeSummary = Management.objects.filter(type='finance',user_id=request.user)
    examinerSummary = Management.objects.filter(type='examiner',user_id=request.user)


    affiliationSummary = Affiliation.objects.filter(user_id=request.user)

    document = Document.objects.filter(user_id=request.user,type="affiliation document")
    payment_list = Payment.objects.filter(user_id=request.user,type='affiliation_payment')


    context = {'institutionSummary':institutionSummary, 'institutionTypeSummary':institutionTypeSummary,'institutionHeadSummary':institutionHeadSummary,'businessDetailSummary':businessDetailSummary,'registrarSummary':registrarSummary,'financeSummary':financeSummary,'examinerSummary':examinerSummary,'affiliationSummary':affiliationSummary,'documents':document,'payments':payment_list}
    return render(request,'crud/summary.html',context)




@login_required(login_url="/authenticate/login")
def affiliation_completed(request):

    institution = Institution.objects.filter(user_id=request.user)
    payment = Payment.objects.filter(user_id=request.user, type='affiliation_payment')
    management = Management.objects.filter(user_id=request.user)
    document = Document.objects.filter(user_id=request.user, type='affiliation document')

    # print(document)

    email_subject = "NABPTEX AFFILIATION"
    message = "Your application for Affiliation with NABPTEX has been submitted sucessfully and is pending review.You may contact us for any other details. Thank you."
    to_email = request.user.email

  

    
    if request.method == 'POST' and institution and payment and management and document:
        type = 'affiliation'
        status = 'pending'

        status_object = Status.objects.filter(user_id=request.user, type=type)
        # print(status_object)
        # email = EmailMessage(email_subject, message, to=[to_email])

        if status_object:
            Institution.objects.filter(user_id=request.user).update(status=status,type=type)
            return render(request,'crud/affiliation_completed.html')

        else:
            status_instance = Status(type=type,status=status)
            status_instance.user = request.user
            status_instance.save()
            

            # ****************
            Institution.objects.filter(user_id=request.user).update(status=status,type=type)
            # ****************

            contacts = Contact_Person.objects.get(user_id=request.user.id)
            contact = contacts.contact
            
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

            sendSms(contact,"Your application for Affiliation with NABPTEX has been submitted sucessfully and is pending review. Thank you.")

            return render(request,'crud/affiliation_completed.html')


    else:
        return render(request,'crud/affiliation_incomplete.html')

    

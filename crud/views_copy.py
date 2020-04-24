from django.shortcuts import render,redirect, Http404, get_object_or_404
from authentication.models import Institution, Institution_Type, Business_Details, Affiliation, test_data, Institution_Head, Document, Payment, Management, Status, Contact_Person
from django.utils import six 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from authentication.functions import sendSms
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url="/authenticate/login")
def institution(request):

    if not request.user.is_authenticated:
        raise Http404

    institutionSummary = Institution.objects.filter(user_id=request.user)
    institutionHeadSummary = Institution_Head.objects.filter(user_id=request.user)
    businessDetailSummary = Business_Details.objects.filter(user_id=request.user)


    if request.method == 'POST':

        institution_name = request.POST['institution']
        digital_address = request.POST['digital']
        town = request.POST['city']
        region = request.POST['region']
        postal_address = request.POST['postal']
        email = request.POST['email']
        contact = request.POST['contact']
        website = request.POST['website']

        designation_of_head = request.POST['head_designation']
        name_of_head = request.POST['head_name']
        contact_of_head = request.POST['head_phone_number']
        email_of_head = request.POST['head_email']


    
        institution_type_item = request.POST
        item = dict(six.iterlists(institution_type_item))

        for inst_type_item in item['inst_type']:

            inst_type_instance = Institution_Type(type=inst_type_item)
            inst_type_instance.user = request.user
            inst_type_instance.save()

        agency_type = request.POST['business']
        agency_name = request.POST['agency_name']
        # registration_date = request.POST['registration_date']
        registration_number = request.POST['registration_number']


        
        institution_instance = Institution(name=institution_name,postal_address=postal_address,contact=contact,email=email,website=website,digital_address=digital_address,region=region,town=town)
        institution_head_instance = Institution_Head(name=name_of_head,designation=designation_of_head,contact=contact_of_head,email=email_of_head)
        # business_registration_instance = Business_Details(agency_name=agency_name,registration_date=registration_date,registration_number=registration_number,agency_type=agency_type)
        business_registration_instance = Business_Details(agency_name=agency_name,registration_number=registration_number,agency_type=agency_type)

        

        institution_instance.user = request.user
        institution_instance.save()

        institution_head_instance.user = request.user
        institution_head_instance.save()

        business_registration_instance.user = request.user
        business_registration_instance.save()


        return redirect('management')

    elif institutionSummary:
        context = {'institutionSummary':institutionSummary,'institutionHeadSummary':institutionHeadSummary,'businessDetailSummary':businessDetailSummary}
        return render(request,'crud/institution1.html', context)


    else:
        return render(request,'crud/institution1.html')

    

@login_required(login_url="/authenticate/login")
def management(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == 'POST':
        registrar_name = request.POST['re_name']
        registrar_designation = request.POST['re_designation']
        contact = request.POST['re_contact']
        contact_1 = request.POST['re_contact_1']
        email = request.POST['re_email']
        # completion_year = request.POST['re_completion_date']
        registrar_type = 'registrar'


        ex_name = request.POST['ex_name']
        ex_designation = request.POST['ex_designation']
        ex_contact = request.POST['ex_contact']
        ex_contact_1 = request.POST['ex_contact_1']
        ex_email = request.POST['ex_email']
        # completion_year = request.POST['re_completion_date']
        ex_type = 'examiner'



        fo_name = request.POST['fin_name']
        fo_designation = request.POST['fin_designation']
        fo_contact = request.POST['fin_contact']
        fo_contact_1 = request.POST['fin_contact_1']
        fo_email = request.POST['fin_email']
        # completion_year = request.POST['re_completion_date']
        fo_type = 'finance'


        registrar_instance = Management(designation=registrar_designation,primary_contact=contact,email=email,name=registrar_name,contact=contact_1,type=registrar_type)
        registrar_instance.user = request.user
        registrar_instance.save()


        fo_instance = Management(designation=fo_designation,primary_contact=fo_contact,email=fo_email,name=fo_name,contact=fo_contact_1,type=fo_type)
        fo_instance.user = request.user
        fo_instance.save()


        ex_instance = Management(designation=ex_designation,primary_contact=ex_contact,email=ex_email,name=ex_name,contact=ex_contact_1,type=ex_type)
        ex_instance.user = request.user
        ex_instance.save()

        return redirect('affiliate')


    else:
        return render(request,'crud/management.html', {})


@login_required(login_url="/authenticate/login")
def affiliate(request):

    if not request.user.is_authenticated:
        raise Http404

    if request.method == 'POST':

        # data = request.POST
        # item = dict(six.iterlists(data))


        # for itemValue in item['mentor']:

        #     affiliation_instance = Affiliation(affiliate_name=itemValue)
        #     affiliation_instance.user = request.user
        #     affiliation_instance.save()

        return redirect('document_upload')

    else:
        return render(request,'crud/affiliate.html', {})


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
    payment_list = Payment.objects.filter(user_id=request.user)


    context = {'institutionSummary':institutionSummary, 'institutionTypeSummary':institutionTypeSummary,'institutionHeadSummary':institutionHeadSummary,'businessDetailSummary':businessDetailSummary,'registrarSummary':registrarSummary,'financeSummary':financeSummary,'examinerSummary':examinerSummary,'affiliationSummary':affiliationSummary,'documents':document,'payments':payment_list}
    return render(request,'crud/summary.html',context)




@login_required(login_url="/authenticate/login")
def affiliation_completed(request):

    institution = Institution.objects.filter(user_id=request.user)
    payment = Payment.objects.filter(user_id=request.user)
    management = Management.objects.filter(user_id=request.user)
    document = Document.objects.filter(user_id=request.user)
    

    
    if request.method == 'POST' and institution and payment and management and document:
        type = 'affiliation'
        status = 'pending'

        status_object = Status.objects.filter(user_id=request.user)
        # print(status_object)

        if status_object:
            return render(request,'crud/affiliation_completed.html')

        else:
            status_instance = Status(type=type,status=status)
            status_instance.user = request.user
            status_instance.save()
            

            # ****************
            Institution.objects.filter(user_id=request.user).update(status='pending',type="affiliation")
            # ****************

            contacts = Contact_Person.objects.get(user_id=request.user.id)
            contact = contacts.contact

            sendSms(contact,"Your application for Affiliation with NABPTEX has been submitted sucessfully and is pending review. Thank you.")

            return render(request,'crud/affiliation_completed.html')


    else:
        return render(request,'crud/affiliation_incomplete.html')

    

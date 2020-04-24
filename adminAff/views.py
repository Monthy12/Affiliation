from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import Institution, Institution_Type, Business_Details, Affiliation, test_data, Institution_Head, Document, Payment, Management, Status, Programme, Department, Lecture_Room, Facility, Library_Books, Laboratory, Examination_Unit, Contact_Person
from itertools import chain
from django.contrib.auth.decorators import login_required
from authentication.decorators import unauthenticated_user, allowed_users
from authentication.functions import sendSms
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.

@login_required(login_url="/authenticate/login")
@allowed_users(allowed_roles=['admin'])
def home(request):

    affiliation = Status.objects.filter(type='affiliation')
    affiliation_pending = Status.objects.filter(status='pending',type='affiliation')
    affiliation_approved = Status.objects.filter(status='approved',type='affiliation')


    totalAffiliation = affiliation.count()
    totalAffiliationPending = affiliation_pending.count()
    totalAffiliationApproved = affiliation_approved.count()


    mounting = Status.objects.filter(type='mounting')
    mounting_pending = Status.objects.filter(status='pending',type='mounting')
    mounting_approved = Status.objects.filter(status='approved',type='mounting')


    totalMounting = mounting.count()
    totalMountingPending = mounting_pending.count()
    totalMountingApproved = mounting_approved.count()


    context = {'totalAffiliation':totalAffiliation,'totalAffiliationPending':totalAffiliationPending,'totalAffiliationApproved':totalAffiliationApproved,'totalMounting':totalMounting,'totalMountingPending':totalMountingPending,'totalMountingApproved':totalMountingApproved}
    return render(request,'adminAff/dashboard.html',context)



@login_required(login_url="/authenticate/login")
@allowed_users(allowed_roles=['admin'])
def admin_affiliation(request):
    institutions = Institution.objects.all()

    context = {'institutions':institutions}
    return render(request,'adminAff/admin_affiliation.html',context)


@login_required(login_url="/authenticate/login")
def admin_programme(request):
    programmes = Programme.objects.all()

    context = {"programmes":programmes}
    return render(request, 'adminAff/admin_programme.html',context)



@allowed_users(allowed_roles=['admin'])
def client_details(request, id):

    user = User.objects.get(id=id)

    email_subject = "NABPTEX AFFILIATION"
    message = "Your application for Affiliation with NABPTEX has been approved. Kindly logon to the portal and begin the process of mounting a programme.You may contact us for any other details. Thank you."
    to_email = user.email



    if request.method == 'POST':
        Status.objects.filter(user_id=id,type="affiliation").update(status='approved')
        # *******
        Institution.objects.filter(user_id=id,type="affiliation").update(status='approved')
        # *******

        contacts = Contact_Person.objects.get(user_id=id)
        contact = contacts.contact
        
        sendSms(contact,"Your application for Affiliation with NABPTEX has been approved. Kindly logon to the portal and begin the process of mounting a programme. Thank you.")

        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()

        return redirect('admin_home')
    
    

    institutions = Institution.objects.get(user_id=id)
    institution_head = Institution_Head.objects.get(user_id=id)
    institution_types = Institution_Type.objects.filter(user_id=id)
    business_detail = Business_Details.objects.get(user_id=id)
    registrars = Management.objects.filter(user_id=id, type='registrar')
    finanaces = Management.objects.filter(user_id=id, type='finance')
    examiners = Management.objects.filter(user_id=id, type='examiner')
    documents = Document.objects.filter(user_id=id,type="affiliation document")
    payments = Payment.objects.filter(user_id=id, type="affiliation_payment")


    context = {'institutions':institutions,'institution_head':institution_head,'institution_types':institution_types,'business_detail':business_detail,'registrars':registrars,'finanaces':finanaces,'examiners':examiners,'documents':documents,'payments':payments}
    return render(request, 'adminAff/client_affiliation.html', context)




@login_required(login_url="/authenticate/login")
@allowed_users(allowed_roles=['admin'])
def decline(request,id):
    user = User.objects.get(id=id)
    
    if request.method == 'POST':
        message = request.POST['message_decline']
        to_email = user.email
        email_subject = "NABPTEX AFFILIATION"

        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()


        return redirect('admin_home')

    return render(request,'adminAff/admin_decline.html')






@login_required(login_url="/authenticate/login")
@allowed_users(allowed_roles=['admin'])
def programme_client_details(request, id):

    user = User.objects.get(id=id)

    email_subject = "MOUNT A PROGRAMME WITH NABPTEX"
    message = "Your application for mounting a Programme with NABPTEX has been approved. You may contact us for any other details. Thank you."
    to_email = user.email

    if request.method == 'POST':
        Status.objects.filter(user_id=id,type="mounting").update(status='approved')
        # *******
        Programme.objects.filter(user_id=id).update(status='approved')
        # *******

        contacts = Contact_Person.objects.get(user_id=id)
        contact = contacts.contact
        
        sendSms(contact,"Your application for mounting a Programme with NABPTEX has been approved. You may contact us for any other details. Thank you.")

        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()

        return redirect('admin_home')

    programmes = Programme.objects.get(user_id=id)
    departments = Department.objects.get(user_id=id)
    lectureRooms = Lecture_Room.objects.get(user_id=id)
    facilitys = Facility.objects.filter(user_id=id)
    libraryBooks = Library_Books.objects.filter(user_id=id)
    laboratorys = Laboratory.objects.filter(user_id=id)
    examinationUnit = Examination_Unit.objects.filter(user_id=id)
    documents = Document.objects.filter(user_id=id, type="mounting document")
    payments = Payment.objects.filter(user_id=id, type="mounting_payment")

    context = {"programmes":programmes,"departments":departments,"lectureRooms":lectureRooms,"facilitys":facilitys,"libraryBooks":libraryBooks,"laboratorys":laboratorys,"examinationUnit":examinationUnit,"documents":documents,"payments":payments}
    return render(request,"adminAff/client_programme.html",context)
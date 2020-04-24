from django.shortcuts import render
from django.http import HttpResponse
from django.utils import six 
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect, Http404, get_object_or_404
from authentication.models import Mentor, Programme, Facility, Lecture_Room, Library_Books, Laboratory, Document, Payment, Examination_Unit, Department, Institution, Status, Contact_Person
from django.contrib.auth.decorators import login_required
from authentication.functions import sendSms
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import departmentForm
# Create your views here.


@login_required(login_url="/authenticate/login")
def mentor(request):

    if not request.user.is_authenticated:
        raise Http404

    if request.method == 'POST':

        data = request.POST
        item = dict(six.iterlists(data))


        itemCount = len(item['mentor'])

        for itemList in range(itemCount):
            mentor_name = item['mentor'][itemList]
            mentor_programme = item['mentor_programme'][itemList]
            mentor_level = item['level'][itemList]

            affiliation_instance = Mentor(mentor_name=mentor_name,mentor_programme=mentor_programme,mentor_level=mentor_level)
            affiliation_instance.user = request.user
            affiliation_instance.save()


        return redirect('mentor')
    else:
        return render(request, 'mounting/mentor.html')


@login_required(login_url="/authenticate/login")
def mount_programme(request):

    if request.method == 'POST':

        level = request.POST['level']
        programme = request.POST['programme']
        inst_name = Institution.objects.get(user_id=request.user)

        # status = Programme.objects.filter(user_id=request.user,status='incomplete')

        # programme_item = status
        # item = dict(six.iterlists(programme_item))

        # print(item)
        # if status == 'incomplete':
        #     Programme.objects.filter(user_id=request.user).update(level=level,programme_name=programme,status="incomplete")

        # else:

        programme_instance = Programme(level=level,programme_name=programme,status="incomplete",inst_name=inst_name)
        programme_instance.user = request.user
        programme_instance.save()
    
        return redirect("department_head")

    else:

        return render(request,'mounting/mount_programme.html')



@login_required(login_url="/authenticate/login")
def department_head(request):

    if request.method == 'POST':
        department_name = request.POST['department_name']
        name_of_head = request.POST['name_of_head']
        highest_qualification = request.POST['highest_qualification']
        head_contact = request.POST['head_contact']
        head_email = request.POST['head_email']
        date_of_appointment = request.POST['appointment_date']

        dept_head_instance = Department(department_name=department_name,highest_qualification=highest_qualification,name_department_head=name_of_head,contact=head_contact,email=head_email,appointment_date=date_of_appointment)
        dept_head_instance.user = request.user
        dept_head_instance.save()

        return redirect('room_detail')

    else:
        departmentHead = departmentForm()
        context = {'form':departmentHead}
        return render(request, 'mounting/department_head.html',context)


@login_required(login_url="/authenticate/login")
def room_detail(request):

    if request.method == 'POST':

        room_dimension = request.POST['room_dimension']
        room_type = request.POST['room_type']

        
        room_instance = Lecture_Room(size=room_dimension, room_type=room_type)
        room_instance.user = request.user
        room_instance.save()



        data = request.POST
        item = dict(six.iterlists(data))

        for itemValue in item['facility']:

            facility_instance = Facility(item_list=itemValue)
            facility_instance.user = request.user
            facility_instance.save()

        return redirect('library')

    return render(request,'mounting/room_detail.html')


@login_required(login_url="/authenticate/login")
def library(request):

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
            library_instance.save()


        return redirect('laboratory')

    else:
        return render(request, 'mounting/library.html')


@login_required(login_url="/authenticate/login")
def laboratory(request):

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
            laboratory_instance.save()


        return redirect('examination_unit')

    else:
        
        return render(request,'mounting/laboratory.html')



@login_required(login_url="/authenticate/login")
def examination_unit(request):

    if request.method == 'POST':
        itemLists = {'itemList': ['Computers','Printers','UPS','Backup System','Cabinets','Reprographic Machines','Safes','Workiing Desk']}

        data = request.POST
        item = dict(six.iterlists(data))

        # print(item)
        itemCount = len(item['exam_quantity'])

        for itemList in range(itemCount):

            exam_instance = Examination_Unit(item=itemLists['itemList'][itemList],quantity=item['exam_quantity'][itemList])
            exam_instance.user = request.user
            exam_instance.save()


        # item = request.POST['exam_choice']
        # quantity = request.POST['exam_quantity']
        # exam_instance = Examination_Unit(item=item,quantity=quantity)
        # exam_instance.user = request.user
        # exam_instance.save()


        return redirect('mount_document')

    else:
        return render(request,'mounting/examination_unit.html')


@login_required(login_url="/authenticate/login")
def mount_document(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['doc_upload']
        documents_name = request.POST['documents_name']
        documents_name_referred = request.POST['doc_name']
        document_type = 'mounting document'


        if documents_name == 'referred':
            documents_name = documents_name_referred

        document_instance = Document(title = documents_name,document = uploaded_file,type=document_type)

        document_instance.user = request.user
        document_instance.save()

        
        return redirect('mount_document')

    document = Document.objects.filter(user_id=request.user,type="mounting document")
    print(document)
    # document = Document.objects.all()
    return render(request,'mounting/mount_document.html',{'documents':document})

@login_required(login_url="/authenticate/login")
def delete_documents(request, pk):

    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('mount_document')


@login_required(login_url="/authenticate/login")
def mount_payment(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['payment_upload']
        payment_name = request.POST['payment_name']

        payment_instance = Payment(type = payment_name, payment = uploaded_file)

        payment_instance.user = request.user
        payment_instance.save()

        return redirect('mount_payment')


    payment_list = Payment.objects.filter(user_id=request.user,type="mounting_payment")

    # return render(request, 'crud/affiliate_payment.html',{'payments':payment_list})

    return render(request,'mounting/mount_payment.html', {'payments':payment_list})


@login_required(login_url="/authenticate/login")
def delete_payments(request, pk):

    if request.method == 'POST':
        payment = Payment.objects.get(pk=pk)
        payment.delete()

    return redirect('mount_payment')


@login_required(login_url="/authenticate/login")
def mount_summary(request):

    programmeSummarys = Programme.objects.filter(user_id=request.user)
    headDepartmentSummarys = Department.objects.filter(user_id=request.user)
    lectureRoomSummarys = Lecture_Room.objects.filter(user_id=request.user)
    facilitySummarys = Facility.objects.filter(user_id=request.user)
    librarySummarys = Library_Books.objects.filter(user_id=request.user)
    laboratorySummarys = Laboratory.objects.filter(user_id=request.user)
    examinationUnitSummarys = Examination_Unit.objects.filter(user_id=request.user)
    
    documents = Document.objects.filter(user_id=request.user,type="mounting document")
    payment_lists = Payment.objects.filter(user_id=request.user,type="mounting_payment")



    context = {'programmeSummarys':programmeSummarys,'headDepartmentSummarys':headDepartmentSummarys,"lectureRoomSummarys":lectureRoomSummarys,"facilitySummarys":facilitySummarys,"librarySummarys":librarySummarys,"laboratorySummarys":laboratorySummarys,"examinationUnitSummarys":examinationUnitSummarys,"documents":documents,"payment_lists":payment_lists}

    return render(request,'mounting/mount_summary.html',context)



def mounted_completed(request):
    
    programme = Programme.objects.filter(user_id=request.user)
    department = Department.objects.filter(user_id=request.user)
    lectureRoom = Lecture_Room.objects.filter(user_id=request.user)
    examinationUnit = Examination_Unit.objects.filter(user_id=request.user)
    document = Document.objects.filter(user_id=request.user, type='mounting document')
    payment = Payment.objects.filter(user_id=request.user, type='mounting_payment')
    

    email_subject = "MOUNT A PROGRAMME WITH NABPTEX"
    message = "Your application for mounting a Programme with NABPTEX has been submitted sucessfully and is pending review.You may contact us for any other details. Thank you."
    to_email = request.user.email

    
    if request.method == 'POST' and programme and department and lectureRoom and examinationUnit and document and payment:
        type = 'mounting'
        status = 'pending'

        status_object = Status.objects.filter(user_id=request.user, type=type)
        print(status_object)

        if status_object:
            return render(request,'mounting/mount_completed.html')

        else:
            status_instance = Status(type=type,status=status)
            status_instance.user = request.user
            status_instance.save()
            

            # ****************
            # Institution.objects.filter(user_id=request.user).update(status='pending',type="affiliation")
            Programme.objects.filter(user_id=request.user).update(status='pending')
            # ****************

            contacts = Contact_Person.objects.get(user_id=request.user.id)
            contact = contacts.contact
            
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

            sendSms(contact,"Your application for mounting a Programme with NABPTEX has been submitted sucessfully and is pending review. Thank you.")

            return render(request,'mounting/mount_completed.html')


    else:
        return render(request,'mounting/mount_incompleted.html')

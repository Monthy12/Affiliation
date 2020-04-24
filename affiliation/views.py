from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.decorators import applicant_only



@login_required(login_url="/authenticate/login")
@applicant_only
def home(request):

    return render(request, 'home.html')
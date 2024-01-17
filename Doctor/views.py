from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import  Contact, Patient, Feed
from django.core.exceptions import ObjectDoesNotExist
from service.models import Hospitalinfo, Appointmentinfo

@login_required
def Home(request):
    return render(request,'Home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def Aboutus(request):
    return render(request,'Aboutus.html', {})

def review(request):
    return render(request,'review.html', {})

def Services(request):
    return render(request,'Services.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['add']
        ins = Contact(username=username,add=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Contactus.html', {})

def Patientde(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        bloodgroup = request.POST['bloodgroup']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        add = request.POST['add']
        symptoms = request.POST['symptoms']
        ename = request.POST['ename']
        relation = request.POST['relation']
        emergencynumber = request.POST['emergencynumber']
        ins = Patient(first_name=first_name, lastname=lastname, gender=gender, date_of_birth=date_of_birth, marital_status=marital_status, bloodgroup=bloodgroup, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, add=add, symptoms=symptoms, ename=ename, relation=relation, emergencynumber=emergencynumber)
        ins.save()
        print("ok")
    return render(request,'Patient.html', {})

def Priscription(request):
    # Fetch only approved appointments
    approved_appointments = Apps.objects.filter(is_approved=True)

    context = {'approved_appointments': approved_appointments}
    return render(request, 'Priscription.html', context)

def Feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['msg']
        ins = Feed(name=name,msg=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Feedback.html', {})

def Emergency(request):
    return render(request,'Emergency.html', {})

def Dash(request):
    dashdata = Hospitalinfo.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            dashdata = Hospitalinfo.objects.filter(location__icontains=se)
    context = {'dash': dashdata}
    return render(request, 'Hospitalinfo.html', context)

def Dash1(request):
    dashdata1 = Appointmentinfo.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            dashdata1 = Appointmentinfo.objects.filter(hospitalname__icontains=se)
    context = {'dash1': dashdata1}
    return render(request, 'Appointmentinfo.html', context)


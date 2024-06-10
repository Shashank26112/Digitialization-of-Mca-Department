from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import *
from django.core.exceptions import ObjectDoesNotExist

@login_required
def Home(request):
    return render(request,'home.html', {})

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phno = request.POST.get('phno')

        new_user = User.objects.create_user(username, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('login')
    return render(request,'register.html', {})

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
    return render(request,'login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login')

def Adddetails(request):
    if request.method == "POST":
        student_name = request.POST['student_name']
        branch = request.POST['branch']
        yop = request.POST['yop']

        ins = Add_Details(student_name=student_name, branch=branch, yop=yop)
        ins.save()
        print("ok")
    return render(request,'adddetails.html', {})

def Searchalumini(request):
    aluminidata = Add_Details.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            aluminidata = Add_Details.objects.filter(student_name__icontains=se)
    context = {'Searchalumini': aluminidata}
    return render(request, 'searchdetails.html', context)
    
def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['message']
        ins = Contact(username=username,message=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'contactus.html', {})

def Coursedet(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        add = request.POST['add']
        course = request.POST['course']
        ins = Course(first_name=first_name, lastname=lastname, gender=gender, date_of_birth=date_of_birth, marital_status=marital_status, email=email, phonenumber=phonenumber, add=add, course=course)
        ins.save()
        print("ok")
    return render(request,'course.html', {})

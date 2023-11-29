from django.shortcuts import render, redirect
from .models import Member

# Create your views here.


def register(request):
    if request.method == 'POST':
        member = Member(firstName=request.POST['firstName']
                 ,lastName=request.POST['lastName']
                 ,emailAddress=request.POST['emailAddress']
                 ,password=request.POST['password']
                 ,company=request.POST['company']
                 ,phoneNumber=request.POST['company'])
        member.save()
        return redirect('/')

    else:
        return render(request, 'register.html')



def index(request):
    if request.method == 'POST':
         if Member.objects.filter(
                #  firstName=request.POST['firstName']
                # ,lastName=request.POST['lastName']
                 emailAddress=request.POST['emailAddress']
                ,password=request.POST['password']).exists():
                # ,company=request.POST['company']
                # ,phoneNumber=request.POST['company']).exists():
            member = Member.objects.get(
                # firstName=request.POST['firstName']
                # ,lastName=request.POST['lastName']
                 emailAddress=request.POST['emailAddress']
                ,password=request.POST['password'])
                # ,company=request.POST['company']
                # ,phoneNumber=request.POST['company'])
            return render(request, 'booking.html',{'member': member})
         else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')


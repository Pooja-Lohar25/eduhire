from django.shortcuts import render,redirect
from django.contrib import messages
from .models import users


# Create your views here.
def index(req):
    return render(req,'index.html')

def register(req):
    if req.method=='POST':
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        phone = req.POST['no.']
        pswrd = req.POST['pass']
        cpswrd = req.POST['cpass']
        if pswrd==cpswrd:
            if users.objects.filter(email=email).exists():
                messages.info(req,'email taken')
                return redirect('register')
            else:
                user = users.objects.create(fname=fname,lname=lname,email=email,password = pswrd,phone=phone)
                user.save()
                messages.info(req,'user created')
                return redirect('login')

        else:
            messages.info(req,'password not matched')
        return redirect('register')
    else:
        return render(req,'signup.html')


def login(req):
    if req.method=='POST':
        mobemail = req.POST['mobemail']
        pswrd = req.POST['pass']
        usermail = users.objects.filter(email = mobemail,password = pswrd).exists()
        if usermail:
            return redirect('/')

        else:
            messages.info(req,"invalid credentials")
            return redirect('login')
    else:
        return render(req,'login.html')
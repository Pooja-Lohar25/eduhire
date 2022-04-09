from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(req):
    if req.method=='POST':
        fname = req.POST['fname']
        lname = req.POST['lname']
        usernm = req.POST['user']
        email = req.POST['email']
        pswrd = req.POST['pass']
        cpswrd = req.POST['cpass']
        if pswrd==cpswrd:
            if User.objects.filter(username=usernm).exists():
                messages.info(req,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = usernm,password = pswrd,email=email,first_name = fname, last_name = lname)
                user.save()
                messages.info(req,'user created')
                return redirect('register')

        else:
            messages.info(req,'password not matched')
        return redirect('/')
    else:
        return render(req,'register.html')
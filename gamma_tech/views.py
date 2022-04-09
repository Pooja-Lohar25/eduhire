from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Candidate

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
        cur_sal = req.POST['cur_sal']
        domain = req.POST['domain']
        exp_sal = req.POST['exp_sal']
        exp = req.POST['exp']
        city = req.POST['city']
        state =req.POST['state']

        if pswrd==cpswrd:
            if Candidate.objects.filter(email=email).exists():
                messages.info(req,'email taken')
                return redirect('register')
            else:
                user = Candidate.objects.create(fname=fname,lname=lname,email=email,password = pswrd,phone=phone,cur_sal = cur_sal,domain=domain,exp_sal=exp_sal,experience = exp,city=city,state=state)
                user.save()
                
                return redirect('login')

        else:
            messages.info(req,'password not matched')
        return redirect('register')
    else:
        return render(req,'signup.html')


def login(req):
    
    if req.method=='POST':
        mobemail = req.POST['email']
        pswrd = req.POST['pass']
        usermail = Candidate.objects.filter(email = mobemail,password = pswrd).exists()
        if usermail:
            return redirect('/')

        else:
            messages.info(req,"invalid credentials")
            return redirect('login')
    else:
        return render(req,'login.html')
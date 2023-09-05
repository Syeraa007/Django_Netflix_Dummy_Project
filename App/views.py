from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from App.forms import *
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def join(request):
    d={'UFO':Users(),'PFO':Profiles()}
    if request.method=='POST' and request.FILES:
        UFD=Users(request.POST)
        PFD=Profiles(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            UUFO=UFD.save(commit=False)
            pswd=UFD.cleaned_data['password']
            UUFO.set_password(pswd)
            UUFO.save()
            UPFO=PFD.save(commit=False)
            UPFO.username=UUFO
            UPFO.save()
            send_mail('Registration','Congrats..!, Registration is Succefully done in Netflix Application','jacksparrow.7828.007@gmail.com',[UUFO.email],fail_silently=True)
            return HttpResponse('<center><h1><b>Regsitration is successfully done</b></h1></center>')
        else:
            # return HttpResponse('<center><h1><b>Invalid Details Encountered</b></h1></center>')
            return render(request,'error.html')
    return render(request,'join.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def enter(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        AO=authenticate(username=username,password=password)
        if AO:
            if AO.is_active:
                login(request,AO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('No User is Active')
        else:
            # return HttpResponse('<center><h1><b> Invalid Details Encountered </b></h1></center>')
            return render(request,'error.html')
    return render(request,'enter.html')

@login_required
def exit(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def expose(request):
        username=request.session['username']
        UO=User.objects.get(username=username)
        PO=Profile.objects.get(username=UO)
        d={'UO':UO,'PO':PO}
        return render(request,'expose.html',d)

@login_required
def replace(request):
    if request.method=='POST':
        pswd=request.POST['password']
        username=request.session['username']
        UO=User.objects.get(username=username)
        UO.set_password(pswd)
        UO.save()
        return HttpResponse('<center><h1><b> Password Changed Successfully </b></h1></center>')
    return render(request,'replace.html')

def clear(request):
    if request.method=='POST':
        un=request.POST['username']
        pw=request.POST['password']
        LUO=User.objects.filter(username=un)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save
            return HttpResponse('<center><h1><b>Password Reset done successfully </b></h1></center>')
        else:
            return HttpResponse('<center><h1><b> Please Enter a valid username </b></h1></center>')
    return render(request,'clear.html')

def tiger(request):
    return render(request,'tiger.html')

def antony(request):
    return render(request,'antony.html')

def wednesday(request):
    return render(request,'wednesday.html')

def japan(request):
    return render(request,'japan.html')

def og(request):
    return render(request,'og.html')

def movies(request):
    return render(request,'movies.html')

def anime(request):
    return render(request,'anime.html')

def show(request):
    return render(request,'show.html')

def originals(request):
    return render(request,'originals.html')

def drama(request):
    return render(request,'drama.html')

def documentaries(request):
    return render(request,'documentaries.html')

def kid(request):
    return render(request,'kid.html')
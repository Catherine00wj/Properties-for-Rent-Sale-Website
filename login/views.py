from django.shortcuts import render,get_object_or_404,redirect
from register import models

def login(request):
    if request.method=="POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        Error='Some information miss'
        if not(username and password):
            return render(request,'login/login.html',locals())
        Error='No this username exist, rewrite please'
        usern=models.UserD.objects.filter(username=username)
        if not usern:
            return render(request, 'login/login.html', locals())
        passw=models.UserD.objects.get(username=username).password
        if password!=passw:
            Error='Username and password do not match'
            return render(request, 'login/login.html', locals())
        if models.UserD.objects.get(username=username).legal==0:
            Error="Sorry ,you have not confirmed your email, check your mailbox firset"
            return render(request, 'login/login.html', locals())
        request.session['userid']=models.UserD.objects.get(username=username).pk
        name=models.UserInfor.objects.get(Uid_id=models.UserD.objects.get(username=username).pk).givenname
        request.session['givenname']=name
        return redirect('/Search/home')
    return render(request, 'login/login.html', locals())

def logoff(request):
    userid=request.session.get('userid',None)
    if not userid:
        return redirect('/login/')
    else:
        request.session.flush()
    return redirect('/login/')
from django.shortcuts import get_object_or_404,render
from register import models
from .models import  UserD
from register import forms
from .models import UserInfor
from django.shortcuts import HttpResponse,redirect
# Create your views here.
from mysite import settings
import random
def index(request):
    # if request.method=="POST":
    #     print("12313123123")
    #     username=request.POST.get("username",None)
    #     password=request.POST.get("password",None)
    #     models.UserD.objects.create(username=username,password=password)
    #
    #     userid=get_object_or_404(UserD,username=username).pk
    #     print(userid)
    #     models.UserInfor.objects.create(Uid_id=userid)
    #     user_list=models.UserD.objects.all()
    # print(user_list)
    # return render(request, "register/index.html", {"user":user_list})
    wrong=request.session.get('givenname',None)
    name=request.session.get('userid',None)
    print(wrong,name)

    return render(request,"register/index.html",locals())

def userinfoin(request):
    userid = request.session.get('id', None)
    number=request.session.get('number',None)
    userforms=forms.UserInforform()
    familyname = request.POST.get('familyname', None)
    givenname = request.POST.get('givenname', None)
    emailadd = request.POST.get('email', None)
    job = request.POST.get('job', None)
    mobilenum = request.POST.get('mobile', None)
    birthday = request.POST.get('birthday', None)
    if request.method=="POST":
        errormessage ="some information missing or wrong captcha,try again"
        userforms=forms.UserInforform(request.POST)
        if userforms.is_valid() and userid!=None and givenname!=None and familyname!=None and emailadd!=None and job!=None and mobilenum!=None and birthday!=None:

            gender=userforms.cleaned_data['gender']

            if len(birthday)!=10 or birthday[4]!='-' or birthday[7]!='-' or not birthday[:4].isdigit or not birthday[5:7].isdigit or not birthday[8:].isdigit or (int(birthday[5:7])<=0) or int(birthday[5:7])>12 or int(birthday[8:])<=0 or int(birthday[8:])>=31:
                errormessage="wrong birthday,check again"
                return render(request,"register/userinforin.html",locals())
            emailcheck=UserInfor.objects.filter(emailadd=emailadd)
            if emailcheck:
                errormessage="sorry ,this email has been used"
                return render(request,"register/userinforin.html",locals())
            UserInfor.objects.create(birthday=birthday,Uid_id=userid,familyname=familyname,givenname=givenname,emailadd=emailadd,job=job,mobilenum=mobilenum,gender=gender)
            email(emailadd,number)
            return redirect('/register/')

    return render(request,"register/userinforin.html",locals())
def register(request):
    if request.method=="POST":
        wrong="some information missing or wrong captcha,try again"
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        form=forms.Registerform(request.POST)
        if form.is_valid() and username!=None and password2!=None and password1!=None:


            print(username)
            if not password2==password1:
                wrong="password not match"
                return render(request,"register/register.html",locals())

            if len(password2)<6:
                wrong="password too sample"
                return render(request, "register/register.html", locals())

            usern=UserD.objects.filter(username=username)
            if usern:
                wrong="username has been used,change one"
                return render(request,"register/register.html",locals())
            number=random.randint(100000,999999)
            models.UserD.objects.create(username=username, password=password1,code=number)
            userid = get_object_or_404(UserD, username=username).pk
            request.session['id']=userid
            request.session['number']=number
            return redirect('/register/userinfoin')


    form=forms.Registerform()

    return render(request,"register/register.html",locals())

def confirm(request):
    error="Sorry, this is a wrong confirm email,try again"
    number=request.GET.get('code',None)
    tryconfirm=models.UserD.objects.filter(code=number)
    if not tryconfirm:
        return render(request,"register/confirm.html",locals())
    tryconfirm.update(legal=1)


    return redirect("/login/login")

def email(email,code):
    from django.core.mail import EmailMultiAlternatives
    print("1231313")
    subject="confrim on registration"
    text_content="Welcome to our website ,this email is to confirm your registration. If it isn't your registration,just ignore it "
    html_content='''<p>Welcome to our website ,this email is to confirm your registration. If it isn't your registration,just ignore it</p>
                    <p>Thank you for confrim your registration on <a href="http://{}/register/confirm?code={}" target=blank>www.livehere.com</a></p>
                    <p>Click this link for confirm</p>
                    '''.format('127.0.0.1:8000', code)
    message=EmailMultiAlternatives(subject,text_content,settings.EMAIL_HOST_USER,[email])
    message.attach_alternative(html_content,"text/html")
    print(html_content)
    message.send()


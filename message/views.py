from django.shortcuts import render

# Create your views here.
from message import models
from .models import Message
from django.http import HttpResponseRedirect

#Post Message function and some default settings when nothing input
def post_message(request):
    id = request.GET.get('id', None)
    if request.method == 'POST':
        uid = request.session.get('userid', None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        phone = request.POST.get("phone",None)
        email_add = request.POST.get("email_add",None)
        messages = request.POST.get("messages",None)
        if first_name =="":
            first_name="Not Provided"
        if last_name =="":
            last_name="Not Provided"
        if phone =="":
            phone =0
        models.Message.objects.create(first_name=first_name,last_name=last_name,post_user=id,current_user=uid,phone=phone,email_add=email_add,messages=messages)


    return render(request, "send_message.html")

#display message
def show_message(request):
    uid = request.session.get('userid', None)
    mes_list = Message.objects.filter(post_user=uid)

    return render(request, "inbox.html", {"mes": mes_list})

#delete message
def del_message(request):
    id = request.GET.get('id', None)
    infor = Message.objects.get(pk=id)
    infor.delete()

    return HttpResponseRedirect("/message/inbox/")

#Reply Message function and some default settings when nothing input
def reply_message(request):
    id = request.GET.get('id', None)
    if request.method == 'POST':
        uid = request.session.get('userid', None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        phone = request.POST.get("phone",None)
        email_add = request.POST.get("email_add",None)
        messages = request.POST.get("messages",None)
        if first_name =="":
            first_name="Not Provided"
        if last_name =="":
            last_name="Not Provided"
        if phone =="":
            phone =0
        models.Message.objects.create(first_name=first_name,last_name=last_name,post_user=id,current_user=uid,phone=phone,email_add=email_add,messages=messages)

    return render(request, "reply_message.html")
from django.shortcuts import render
from InforRealease import models
from .models import ResourceInfor
from django.shortcuts import HttpResponse, redirect

from django.core.files.base import ContentFile
from django.conf import settings
import os
from comment.models import Comment
def add_resource(request):

    if request.method == "POST":
        uid = request.session.get('userid',None)
        city = request.POST.get("city", None)
        community = request.POST.get("community", None)
        address = request.POST.get("address", None)
        property = request.POST.get("property", None)
        type = request.POST.get("type", None)
        area = request.POST.get("area", None)
        bedrooms = request.POST.get("bedrooms", None)
        bathrooms = request.POST.get("bathrooms", None)
        parking = request.POST.get("parking", None)
        expectmoney = request.POST.get("expectmoney", None)
        phone = request.POST.get("phone", None)
        description = request.POST.get("description", None)
        imgs = request.FILES.getlist("img")

        # for file in imgs:
        #     print(file)


        # img = ResourceInfor(img_url=request.FILES.get('img'))
        # img.save()


        # process the directory of the photos and save them in the table in the database.

        new_resource = models.ResourceInfor.objects.create(uid=uid, city=city, community=community, address=address, property=property, type=type, area=area, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking, expectmoney=expectmoney, phone=phone, description=description)

        try:
            img_paths = ""
            for i in range(0, len(imgs)):
                img = imgs[i]
                file_sub_name = "img/" + str(new_resource.id)+"_"+ str(i)+"_" +img.name
                filename = settings.MEDIA_URL[1:len(settings.MEDIA_URL)] + file_sub_name
                fout = open(filename, "wb")
                file_content = ContentFile(img.read())
                for chunk in file_content.chunks():
                    fout.write(chunk)
                fout.close()
                img_paths += file_sub_name + ";"
                # i += 1

            new_resource.img = img_paths
            new_resource.save()
        except Exception as e:
            new_resource.delete()
            raise e

    return render(request, "resources.html")



def view_all_resources(request):
    aa = models.ResourceInfor.objects.all()
    for resource in aa :
        # if len(resource.img)>0:
        #only display the first photo in the record.
        resource.img = resource.img.strip(';').split(';')[0]

    return render(request, "resources_all.html", {"ResourceInfor": aa})



def view_detail(request):
    id = request.GET.get('id', None)
    get_name = request.session.get('givenname', None)
        # get house info by resource id
    resource_detail = models.ResourceInfor.objects.get(id=id)
    resource_detail.img = resource_detail.img.strip(';').split(';')
    if request.method == 'POST':
        text = request.POST.get("text", None)
        mark = request.POST.get("mark", None)
        Comment.objects.create(name=get_name, pos_id = id,text=text, mark = mark)

    post_list = Comment.objects.filter(pos_id=id).values()

    return render(request, "resource_detail.html", {"ResourceDetail":resource_detail,"comment":post_list})

# only show the information posted by the user
def view_my_resource(request):
    results = []
    if request.method == "GET":
        uid = request.session.get('userid', None)
        results = models.ResourceInfor.objects.filter(uid=uid)
        for resource in results:
            # if len(resource.img)>0:
            resource.img = resource.img.strip(';').split(';')[0]

    return render(request, "my_resources.html", {"ResourceInfor": results})

# the users can only delete the information posted by  themselves
def delete_resource(request):
    if request.method == "GET":
        uid = request.session.get('userid', None)
        id = request.GET.get('id',None)
        objs = models.ResourceInfor.objects.filter(uid=uid, id=id)
        objs.delete()
    return view_my_resource(request)

# def yimi(request):
#     #return HttpResponse('Hello yimi!')   #方法一： 直接传回去一个字符串
#     return render(request, "home.html")

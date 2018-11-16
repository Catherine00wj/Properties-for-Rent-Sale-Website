from django.shortcuts import render

# Create your views here.

from InforRealease import models

from django.http import HttpResponse

#------------ Search information according to the input inforamtion return the matching results -------------------
def search_result(request):
    if request.method == "POST":
        city = request.POST.get("city", None).lower()
        bedrooms = request.POST.get("bedrooms", None).lower()
        bathrooms = request.POST.get("bathrooms", None).lower()
        parking = request.POST.get("parking", None).lower()
        # expectmoney = request.POST.get("expectmoney", None)
        community = request.POST.get("community", None).lower()
        search = request.POST.get("search", None).lower()
        if search != None:
            aa = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking,
                                                     community=community ,type= "rent").filter(description__contains=search)
            if len(aa) != 0:
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            else:
                #-------if there is no matching information, then will return the hole information of renting house-----
                aa = models.ResourceInfor.objects.all().filter(type= "rent")
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            return render(request, "search.html", {"Searchall": aa})
        if search == None:
            aa = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking,community = community , type="rent")
            if len(aa) != 0:
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            else :
                aa = models.ResourceInfor.objects.all().filter(type = "rent")
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            return render(request, "search.html", {"Searchall": aa})
    aa = models.ResourceInfor.objects.filter(type = "rent")
    for resource in aa :
        # if len(resource.img)>0:
        resource.img = resource.img.strip(';').split(';')[0]
    return  render(request, "search.html", {"Searchall": aa})

# def view_all_search(request):
#     aa = models.ResourceInfor.objects.all()
#     for resource in aa :
#         # if len(resource.img)>0:
#         resource.img = resource.img.strip(';').split(';')[0]
#
#     return render(request, "search.html", {"Searchall": aa})
#-------home page wigh search bar and information display-------------------------------
#-------search the input information from the database and return matching information------------
def home(request):
    if request.method == "POST":
        city = request.POST.get("city", None).lower()
        bedrooms = request.POST.get("bedrooms", None).lower()
        bathrooms = request.POST.get("bathrooms", None).lower()
        parking = request.POST.get("parking", None).lower()
        # expectmoney = request.POST.get("expectmoney", None)
        community = request.POST.get("community", None).lower()
        search = request.POST.get("search", None).lower()
        if len(search) !=0:
            aa = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking,
                                                     community=community , description__contains= search);
            if len(aa) != 0:
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            else:
                aa = models.ResourceInfor.objects.all()
                for resource in aa:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            return render(request, "home.html", {"homeall": aa})
        aa = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking,community = community)
        if len(aa) != 0:
            for resource in aa:
                # if len(resource.img)>0:
                resource.img = resource.img.strip(';').split(';')[0]
        else :
            aa = models.ResourceInfor.objects.all()
            for resource in aa:
                # if len(resource.img)>0:
                resource.img = resource.img.strip(';').split(';')[0]
        return render(request, "home.html", {"homeall": aa})
    aa = models.ResourceInfor.objects.all()
    for resource in aa :
        # if len(resource.img)>0:
        resource.img = resource.img.strip(';').split(';')[0]
    return  render(request, "home.html", {"homeall": aa})
    #return HttpResponse('Hello yimi!')   #方法一： 直接传回去一个字符串


